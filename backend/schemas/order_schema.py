from pydantic import BaseModel


class OrderCreate(BaseModel):
    product_ids: list[int]


class OrderResponse(BaseModel):
    status: str
    message: str
