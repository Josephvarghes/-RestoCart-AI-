from sqlalchemy import Column, Float, Integer, String

from db.base import Base


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String)
    price = Column(Float)
    category = Column(String, default="General")
    stock = Column(Integer, default=10)
    is_available = Column(Integer, default=1)
