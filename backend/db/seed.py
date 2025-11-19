from db.session import SessionLocal
from models.product_model import Product

def seed_sample_products():
    db = SessionLocal()
    try:
        if db.query(Product).first() is None:
            sample_products = [
                {"name": "Wireless Mouse", "description": "Smooth control", "price": 499, "category": "Electronics"},
                {"name": "Gaming Keyboard", "description": "RGB lighting", "price": 1599, "category": "Electronics"},
                {"name": "Bluetooth Speaker", "description": "Deep bass", "price": 999, "category": "Audio"},
                {"name": "USB-C Cable", "description": "Fast charging", "price": 199, "category": "Accessories"},
                {"name": "Laptop Stand", "description": "Ergonomic design", "price": 699, "category": "Office"},
                {"name": "Water Bottle", "description": "Hot & cold", "price": 299, "category": "Lifestyle"},
                {"name": "Notebook", "description": "200 pages", "price": 99, "category": "Stationery"},
                {"name": "Desk Lamp", "description": "LED, low power", "price": 399, "category": "Home"},
                {"name": "Pen Drive 32GB", "description": "High speed", "price": 699, "category": "Storage"},
                {"name": "Smart Watch", "description": "Fitness tracking", "price": 1999, "category": "Wearables"},
            ]
            
            for p in sample_products:
                db.add(Product(**p))
            
            db.commit()
            print("Database seeded with 10 sample products!")
        else:
            print("Database already has products – skipping seed.")
    except Exception as e:
        print(f"Error during seeding: {e}")
        db.rollback()
    finally:
        db.close()