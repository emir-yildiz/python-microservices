import asyncpg
from repositories.product_repository import ProductRepository
from services.product_service import ProductService

# Global pool — uygulama ayağa kalkarken set edilir
_db_pool: asyncpg.Pool | None = None

def set_pool(pool: asyncpg.Pool):
    global _db_pool
    _db_pool = pool

def get_product_service() -> ProductService:
    repo = ProductRepository(_db_pool)
    return ProductService(repo)