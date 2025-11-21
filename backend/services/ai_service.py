# from langchain_groq import ChatGroq
# from langchain_core.messages import HumanMessage
# from sqlalchemy.orm import Session
# from models.product_model import Product
# from core.config import settings


# class AIService:

#     @staticmethod
#     def search_products(db: Session, query: str):
#         return db.query(Product).filter(Product.name.ilike(f"%{query}%")).all()

#     @staticmethod
#     def generate_answer(question: str, products):
#         # Build context for AI
#         if not products:
#             context = "No matching products found."
#         else:
#             context = "\n".join([f"- {p.name}: {p.description}" for p in products])

#         prompt = f"""
# You are a product assistant. Answer ONLY using the product data below.

# Product Data:
# {context}

# User Question:
# {question}

# Provide a helpful answer.
# """

#         # FIX 1 → Proper model init (No proxies, no invalid args)
#         llm = ChatGroq(
#             model="llama-3.1-8b-instant",
#             api_key=settings.GROQ_API_KEY,
#             temperature=0.4
#         )

#         # FIX 2 → use invoke(), not llm(prompt)
#         response = llm.invoke([HumanMessage(content=prompt)])

#         # FIX 3 → Grab content safely
#         return response.content
from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage
from sqlalchemy.orm import Session
from models.product_model import Product
from core.config import settings
from services.ai.retriever import semantic_search  # ← NEW IMPORT

class AIService:

    @staticmethod
    def search_products(db: Session, query: str):
        """
        Fallback to keyword search if needed, but prefer semantic.
        For this implementation, we ONLY use semantic search.
        """
        # Use ChromaDB semantic search instead of DB keyword search
        results = semantic_search(query, top_k=3)
        return results  # List of dicts (not ORM objects)

    @staticmethod
    def generate_answer(question: str, products):
        if not products:
            return "I couldn't find any products matching your query. Try asking about electronics, home goods, or fitness items!"

        # products is now list of dicts, not ORM objects
        context = "\n".join([
            f"- {p['name']}: {p['description']} (Price: ${p['price']})"
            for p in products
        ])

        prompt = f"""You are a helpful product assistant for RestoPulse.
Answer the user's question using ONLY the product information below.
Do not invent products, prices, or features.

Products:
{context}

Question: {question}

Answer:"""

        llm = ChatGroq(
            model="llama-3.1-8b-instant",
            api_key=settings.GROQ_API_KEY,
            temperature=0.3
        )

        response = llm.invoke([HumanMessage(content=prompt)])
        return response.content.strip()