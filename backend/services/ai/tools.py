from typing import List, Dict, Optional
from langchain.tools import tool
from sqlalchemy.orm import Session
from db.session import SessionLocal
from models.product_model import Product
from models.order_model import Order
import json

@tool
def check_inventory(item_name: str) -> str:
    """Checks the current stock level and availability of a specific menu item."""
    db = SessionLocal()
    try:
        product = db.query(Product).filter(Product.name.ilike(f"%{item_name}%")).first()
        if not product:
            return f"Item '{item_name}' not found in the menu."
        
        status = "Available" if product.is_available and product.stock > 0 else "Out of Stock"
        return json.dumps({
            "name": product.name,
            "stock": product.stock,
            "price": product.price,
            "status": status
        })
    finally:
        db.close()

@tool
def fetch_kitchen_load() -> str:
    """Returns the current load of the kitchen based on the number of active orders."""
    db = SessionLocal()
    try:
        order_count = db.query(Order).count()
        # Logic: 0-3 orders = Low (Fast), 4-7 = Medium, >8 = High (Busy)
        load_percentage = min(order_count * 10, 100)
        
        status = "Low"
        if load_percentage > 70:
            status = "High (Expect Delays)"
        elif load_percentage > 30:
            status = "Medium"
            
        return json.dumps({
            "active_orders": order_count,
            "load_percentage": load_percentage,
            "status": status
        })
    finally:
        db.close()

@tool
def process_order(items_json: str) -> str:
    """Finalizes and places the order in the system. Input is JSON string of items."""
    # In a real app, this would deduct stock and create an Order record.
    # For the demo, we'll simulate the success.
    try:
        items = json.loads(items_json)
        # Mocking order processing
        item_names = [f"{i['quantity']}x {i['name']}" for i in items]
        return f"Order placed successfully: {', '.join(item_names)}. Sending to kitchen now."
    except Exception as e:
        return f"Error processing order: {str(e)}"

@tool
def calculate_bill(items_json: str) -> str:
    """Calculates the total bill amount including tax for the requested items."""
    db = SessionLocal()
    try:
        items = json.loads(items_json)
        total = 0
        details = []
        for item in items:
            product = db.query(Product).filter(Product.name.ilike(f"%{item['name']}%")).first()
            if product:
                item_total = product.price * item['quantity']
                total += item_total
                details.append({
                    "item": product.name,
                    "price": product.price,
                    "quantity": item['quantity'],
                    "subtotal": item_total
                })
        
        tax = total * 0.05 # 5% tax
        grand_total = total + tax
        
        return json.dumps({
            "items": details,
            "subtotal": total,
            "tax": tax,
            "grand_total": grand_total
        })
    finally:
        db.close()
