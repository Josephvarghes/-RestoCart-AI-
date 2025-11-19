from pydantic import BaseModel

class ProductResponse(BaseModel):
    id: int
    name: str
    description: str
    price: float
    category: str

    class Config:
        orm_mode = True
