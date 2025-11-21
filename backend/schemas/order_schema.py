from pydantic import BaseModel
from typing import List

class OrderCreate(BaseModel):
    product_ids: List[int]

class OrderResponse(BaseModel):
    status: str
    message: str
