from sqlalchemy.orm import Session

from models.product_model import Product


class ProductRepository:
    def get_all(self, db: Session):
        return db.query(Product).all()
