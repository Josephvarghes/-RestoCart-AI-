from sqlalchemy.orm import Session

from models.order_model import Order


class OrderService:
    @staticmethod
    def create_order(db: Session, product_ids: list):
        csv_data = ",".join([str(pid) for pid in product_ids])
        order = Order(product_ids=csv_data)
        db.add(order)
        db.commit()
        db.refresh(order)
        return order
