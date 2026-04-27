from contextlib import asynccontextmanager
from fastapi import FastAPI
import asyncio
import asyncpg
from dependencies.dependencies import set_pool
from routers import product_router
from config import Settings
from exceptions.product_exception import ProductNotFoundException,ProductAlreadyExistsException
from fastapi import Request
from fastapi.responses import JSONResponse
from core.logging import setup_logging,get_logger

settings = Settings()
setup_logging(level=settings.log_level)
logger = get_logger(__name__)

async def periodic_health_check(pool, interval: int = 30):  # ← pool parametre olarak alındı
    while True:
        try:
            await pool.fetchval("SELECT 1")
            logger.info("Health check: ok")
        except Exception as e:
            logger.error("Health check failed: %s", e)
        await asyncio.sleep(interval)

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Uygulama başlarken
    logger.info(f"Uygulama başlatıldı")
    pool = await asyncpg.create_pool(dsn=settings.database_url,min_size=2,max_size=10)
    set_pool(pool)
    task = asyncio.create_task(periodic_health_check(pool, interval=settings.health_check_interval))  # ← pool geçildi
    yield
    # Uygulama kapanırken
    await pool.close()
    logger.info(f"Uygulama kapatılıyor")


app = FastAPI(lifespan=lifespan)
app.include_router(product_router.router)

@app.exception_handler(ProductNotFoundException)
async def not_found_handler(request: Request, exc: ProductNotFoundException):
    return JSONResponse(status_code=404, content={"detail": str(exc)})

@app.exception_handler(ProductAlreadyExistsException)
async def already_exists_handler(request: Request, exc: ProductAlreadyExistsException):
    return JSONResponse(status_code=409, content={"detail": str(exc)})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=settings.app_port, reload=True)