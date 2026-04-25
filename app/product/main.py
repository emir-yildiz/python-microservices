from contextlib import asynccontextmanager
from fastapi import FastAPI
import asyncpg
from dependencies.dependencies import set_pool
from routers import product_router
from config import Settings
from exceptions.product_exception import ProductNotFoundException,ProductAlreadyExistsException
from fastapi import Request
from fastapi.responses import JSONResponse

settings = Settings()

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Uygulama başlarken
    pool = await asyncpg.create_pool(dsn=settings.database_url,min_size=2,max_size=10)
    set_pool(pool)
    yield
    # Uygulama kapanırken
    await pool.close()


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