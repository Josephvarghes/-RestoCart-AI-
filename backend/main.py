from fastapi import FastAPI
from api.v1.routes import product_route
from db.session import engine
from db.base import Base 
from db.seed import seed_sample_products 
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI(title="RestoPulse Backend", version="1.0")

app.include_router(product_route.router, prefix="/api/v1/products", tags=["Products"]) 

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

seed_sample_products()