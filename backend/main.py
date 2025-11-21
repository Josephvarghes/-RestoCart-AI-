from fastapi import FastAPI
from api.v1.routes import product_route, order_router, ai_router
from db.session import engine
from db.base import Base 
from db.seed import seed_sample_products 
from fastapi.middleware.cors import CORSMiddleware 
from utils.chroma_init import init_chroma_db

Base.metadata.create_all(bind=engine)

app = FastAPI(title="RestoPulse Backend", version="1.0")

app.include_router(product_route.router, prefix="/api/v1/products", tags=["Products"])  
app.include_router(order_router.router, prefix="/api/v1/orders", tags=["Orders"])
app.include_router(ai_router.router, prefix="/api/v1/ai", tags=["AI"] )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Vite port
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

seed_sample_products() 
init_chroma_db()