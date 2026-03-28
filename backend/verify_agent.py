import os
from dotenv import load_dotenv
from sqlalchemy.orm import Session
from db.session import SessionLocal, engine
from db.base import Base
from db.seed import seed_sample_products
from services.ai.agent_service import AgentService

# Load environment variables
load_dotenv()

def reset_db():
    print("Resetting database...")
    if os.path.exists("restopulse.db"):
        os.remove("restopulse.db")
    Base.metadata.create_all(bind=engine)
    seed_sample_products()
    print("Database reset and seeded with restaurant menu.")

def test_agent():
    db = SessionLocal()
    session_id = "test_user_123"
    
    print("\n--- Test 1: Simple Order ---")
    q1 = "I want to order 2 classic veg burgers and a fresh lime soda"
    print(f"User: {q1}")
    a1 = AgentService.run_agent(db, session_id, q1)
    print(f"Agent: {a1}")

    print("\n--- Test 2: Out of Stock Item ---")
    q2 = "Actually, can I also get a Pepperoni Feast pizza?"
    print(f"User: {q2}")
    a2 = AgentService.run_agent(db, session_id, q2)
    print(f"Agent: {a2}")

    print("\n--- Test 3: Kitchen Load Check ---")
    # Simulate high load by adding dummy orders
    from models.order_model import Order
    for _ in range(8):
        db.add(Order(product_ids="1,2,3"))
    db.commit()
    
    q3 = "Can I add 3 Hyderabadi Chicken Biryanis to my order?"
    print(f"User: {q3}")
    a3 = AgentService.run_agent(db, session_id, q3)
    print(f"Agent: {a3}")

    db.close()

if __name__ == "__main__":
    reset_db()
    test_agent()
