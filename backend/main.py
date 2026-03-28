from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from api.v1.routes import ai_router, order_router, product_route
from db.base import Base
# Register models
from models.product_model import Product
from models.order_model import Order
from models.chat_model import ChatMessage

from db.seed import seed_sample_products
from db.session import engine
from utils.chroma_init import init_chroma_db

Base.metadata.create_all(bind=engine)

app = FastAPI(title="RestoPulse Backend", version="1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Being more permissive for development to avoid localhost/127.0.0.1 mismatches
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(product_route.router, prefix="/api/v1/products", tags=["Products"])
app.include_router(order_router.router, prefix="/api/v1/orders", tags=["Orders"])
app.include_router(ai_router.router, prefix="/api/v1/ai", tags=["AI"])

seed_sample_products()
init_chroma_db()
