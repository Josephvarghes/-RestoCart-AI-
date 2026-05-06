from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from db.base import Base


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    items = relationship("OrderItem", back_populates="order")
