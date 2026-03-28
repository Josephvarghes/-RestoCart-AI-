from db.session import SessionLocal
from models.product_model import Product


def seed_sample_products():
    db = SessionLocal()
    try:
        if db.query(Product).first() is None:
            sample_products = [
                {
                    "name": "Classic Veg Burger",
                    "description": "Crispy veg patty with lettuce and cheese",
                    "price": 149,
                    "category": "Burgers",
                    "stock": 15,
                    "is_available": 1
                },
                {
                    "name": "Chicken Cheese Burger",
                    "description": "Grilled chicken patty with extra cheese",
                    "price": 199,
                    "category": "Burgers",
                    "stock": 10,
                    "is_available": 1
                },
                {
                    "name": "Margherita Pizza",
                    "description": "Classic tomato and mozzarella",
                    "price": 299,
                    "category": "Pizzas",
                    "stock": 5,
                    "is_available": 1
                },
                {
                    "name": "Pepperoni Feast",
                    "description": "Loaded with spicy pepperoni and cheese",
                    "price": 449,
                    "category": "Pizzas",
                    "stock": 0,  # Mocking out of stock for testing
                    "is_available": 0
                },
                {
                    "name": "Hyderabadi Chicken Biryani",
                    "description": "Authentic spicy dum biryani",
                    "price": 349,
                    "category": "Main Course",
                    "stock": 20,
                    "is_available": 1
                },
                {
                    "name": "Paneer Butter Masala",
                    "description": "Creamy tomato base with soft paneer cubes",
                    "price": 279,
                    "category": "Main Course",
                    "stock": 12,
                    "is_available": 1
                },
                {
                    "name": "French Fries",
                    "description": "Classic salted crispy fries",
                    "price": 99,
                    "category": "Sides",
                    "stock": 30,
                    "is_available": 1
                },
                {
                    "name": "Garlic Bread",
                    "description": "Toasted bread with garlic butter and herbs",
                    "price": 129,
                    "category": "Sides",
                    "stock": 25,
                    "is_available": 1
                },
                {
                    "name": "Chocolate Lava Cake",
                    "description": "Warm cake with a molten chocolate center",
                    "price": 149,
                    "category": "Desserts",
                    "stock": 8,
                    "is_available": 1
                },
                {
                    "name": "Fresh Lime Soda",
                    "description": "Refreshing lemon drink with soda",
                    "price": 79,
                    "category": "Beverages",
                    "stock": 40,
                    "is_available": 1
                },
            ]

            for p in sample_products:
                db.add(Product(**p))

            db.commit()
            print("Database seeded with 10 restaurant products!")
        else:
            print("Database already has products – skipping seed.")
    except Exception as e:
        print(f"Error during seeding: {e}")
        db.rollback()
    finally:
        db.close()
