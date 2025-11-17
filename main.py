from fastapi import FastAPI
from api.v1.routes import product_route
from db.session import engine
from db.base import Base 
from db.seed import seed_sample_products

Base.metadata.create_all(bind=engine)

app = FastAPI(title="RestoPulse Backend", version="1.0")

app.include_router(product_route.router, prefix="/api/v1/products", tags=["Products"])

seed_sample_products()