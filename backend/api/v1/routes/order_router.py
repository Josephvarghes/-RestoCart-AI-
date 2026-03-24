from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.session import SessionLocal
from schemas.order_schema import OrderCreate, OrderResponse
from services.order_service import OrderService

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=OrderResponse)
def place_order(payload: OrderCreate, db: Session = Depends(get_db)):
    OrderService.create_order(db, payload.product_ids)
    return {"status": "success", "message": "Order placed!"}
