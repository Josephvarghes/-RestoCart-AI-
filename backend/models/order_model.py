from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func

from db.base import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    product_ids = Column(String, nullable=False)  # stored as CSV: "1,5,7"
    created_at = Column(DateTime(timezone=True), server_default=func.now())
