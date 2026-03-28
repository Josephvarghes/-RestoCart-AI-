from langchain_groq import ChatGroq
from langchain_classic.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from sqlalchemy.orm import Session

from core.config import settings
from services.ai.tools import check_inventory, fetch_kitchen_load, process_order, calculate_bill
from repositories.chat_repo import ChatRepository

class AgentService:
    @staticmethod
    def get_agent_executor():
        llm = ChatGroq(
            model="llama-3.1-70b-versatile",
            api_key=settings.GROQ_API_KEY,
            temperature=0.1
        )
        
        tools = [check_inventory, fetch_kitchen_load, process_order, calculate_bill]
        
        prompt = ChatPromptTemplate.from_messages([
            ("system", """You are the 'Resto-Manager' AI for RestoPulse. 
            Your goal is to assist customers with orders while managing restaurant constraints.
            
            GUIDELINES:
            1. Always check 'fetch_kitchen_load' before confirming any large or complex order.
            2. Always 'check_inventory' for every item requested by the user.
            3. DECISION LOGIC:
               - If kitchen load is HIGH (>70%), politely warn the user of delays and suggest faster alternatives (like 'Sides' or 'Beverages').
               - If an item is 'Out of Stock', recommend a similar dish from the same category.
               - If valid, use 'calculate_bill' to show the total before asking for final 'process_order' confirmation.
            4. Be professional, helpful, and concise. 
            5. Use tools ONLY when needed. If the user is just saying 'hi', respond normally without tools."""),
            MessagesPlaceholder(variable_name="chat_history"),
            ("human", "{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad"),
        ])
        
        agent = create_openai_tools_agent(llm, tools, prompt)
        return AgentExecutor(agent=agent, tools=tools, verbose=True)

    @staticmethod
    def run_agent(db: Session, session_id: str, user_input: str):
        # 1. Fetch History
        db_history = ChatRepository.get_history(db, session_id)
        chat_history = []
        for msg in db_history:
            if msg.role == "user":
                chat_history.append(HumanMessage(content=msg.content))
            else:
                chat_history.append(AIMessage(content=msg.content))
        
        # 2. Run Executor
        executor = AgentService.get_agent_executor()
        response = executor.invoke({
            "input": user_input,
            "chat_history": chat_history
        })
        
        answer = response["output"]
        
        # 3. Persist Messages
        ChatRepository.add_message(db, session_id, "user", user_input)
        ChatRepository.add_message(db, session_id, "assistant", answer)
        
        return answer
