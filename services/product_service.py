from sqlalchemy.orm import Session
from repositories.product_repo import ProductRepository

repo = ProductRepository()

class ProductService:
    def list_products(self, db: Session):
        return repo.get_all(db)
