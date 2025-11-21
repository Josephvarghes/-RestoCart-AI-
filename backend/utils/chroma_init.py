from sqlalchemy.orm import Session
from db.session import SessionLocal
from models.product_model import Product
from services.ai.retriever import get_or_create_collection

def init_chroma_db():
    db: Session = SessionLocal()
    try:
        products = db.query(Product).all()
        collection = get_or_create_collection()

        # Check if already populated
        if collection.count() == 0:
            ids = [str(p.id) for p in products]
            documents = [f"{p.name}: {p.description}" for p in products]
            metadatas = [
                {
                    "name": p.name,
                    "description": p.description,
                    "price": p.price
                }
                for p in products
            ]
            collection.add(
                ids=ids,
                documents=documents,
                metadatas=metadatas
            )
            print(f"✅ ChromaDB populated with {len(products)} products")
        else:
            print("✅ ChromaDB already initialized")
    finally:
        db.close()