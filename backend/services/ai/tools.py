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
    """
    Finalizes and places the order in the system. 
    Input: items_json (str) - A JSON string representing a list of items. 
    Example: '[{"name": "Margherita Pizza", "quantity": 1}, {"name": "French Fries", "quantity": 2}]'
    """
    db = SessionLocal()
    try:
        items = json.loads(items_json)
        if not items:
            return "Error: No items provided in the order."
            
        # 1. Normalize and Batch Fetch Products
        # Extract names from items
        names = []
        for item in items:
            name = item.get("name") or item.get("item") or item.get("product")
            if name:
                names.append(name)
        
        if not names:
            return "Error: No valid item names found in the order."

        # Fetch all products in one go with row-level locking if possible (SQLite doesn't support with_for_update well but it's good practice)
        # For SQLite, we rely on the transaction serializability.
        products = db.query(Product).filter(Product.name.in_(names)).all()
        product_map = {p.name.lower(): p for p in products}
        
        order_ids = []
        ordered_item_details = []
        
        # 2. Transactional Validation & Update
        for raw_item in items:
            name_input = raw_item.get("name") or raw_item.get("item") or raw_item.get("product")
            quantity = raw_item.get("quantity") or raw_item.get("qty") or 1
            
            product = product_map.get(name_input.lower())
            if not product:
                # Fallback to ilike if direct match fails (less efficient but keeps robustness)
                product = db.query(Product).filter(Product.name.ilike(f"%{name_input}%")).first()
                if not product:
                    return f"Error: Product '{name_input}' not found in our menu."
            
            if product.stock < quantity:
                return f"Error: Insufficient stock for '{product.name}'. Available: {product.stock}, Requested: {quantity}."
            
            # Atomic update
            product.stock -= quantity
            if product.stock <= 0:
                product.stock = 0
                product.is_available = 0
            
            # Record details
            for _ in range(quantity):
                order_ids.append(str(product.id))
            ordered_item_details.append(f"{quantity}x {product.name}")
        
        new_order = Order(
            product_ids=",".join(order_ids)
        )
        db.add(new_order)
        db.commit()
        db.refresh(new_order)
        
        return f"Order placed successfully! Order ID: {new_order.id}. Items: {', '.join(ordered_item_details)}. I have sent this to the kitchen."
    except json.JSONDecodeError:
        return "Error: Invalid JSON format provided for items_json."
    except Exception as e:
        db.rollback()
        return f"Error processing order: {str(e)}"
    finally:
        db.close()

@tool
def calculate_bill(items_json: str) -> str:
    """
    Calculates the total bill amount including tax for the requested items.
    Input: items_json (str) - A JSON string representing a list of items and quantities.
    Example: '[{"name": "Margherita Pizza", "quantity": 1}, {"name": "French Fries", "quantity": 2}]'
    """
    db = SessionLocal()
    try:
        items = json.loads(items_json)
        
        # 1. Batch Fetch
        names = [i.get("name") or i.get("item") or i.get("product") for i in items if i.get("name") or i.get("item") or i.get("product")]
        products = db.query(Product).filter(Product.name.in_(names)).all()
        product_map = {p.name.lower(): p for p in products}

        total = 0
        details = []
        for raw_item in items:
            name_input = raw_item.get("name") or raw_item.get("item") or raw_item.get("product")
            quantity = raw_item.get("quantity") or raw_item.get("qty") or 1
            
            if not name_input:
                continue

            product = product_map.get(name_input.lower())
            if not product:
                 # Fallback
                 product = db.query(Product).filter(Product.name.ilike(f"%{name_input}%")).first()

            if product:
                item_total = product.price * quantity
                total += item_total
                details.append({
                    "item": product.name,
                    "price": product.price,
                    "quantity": quantity,
                    "subtotal": item_total
                })
        
        tax = total * 0.05 # 5% tax
        grand_total = total + tax
        
        return json.dumps({
            "items": details,
            "subtotal": round(total, 2),
            "tax": round(tax, 2),
            "grand_total": round(grand_total, 2)
        })
    except Exception as e:
        return f"Error calculating bill: {str(e)}. Please ensure items are in JSON format: '[{{\"name\": \"...\", \"quantity\": 1}}]'"
    finally:
        db.close()
