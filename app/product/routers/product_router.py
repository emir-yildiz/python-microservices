from fastapi import APIRouter, Depends
from schemas import ProductInsert, ProductDelete,ProductUpdate
from services.product_service import ProductService
from dependencies.dependencies import get_product_service

router = APIRouter(prefix="/product", tags=["product"])

@router.post("/insert", status_code=201)
async def insert_product(
    data: ProductInsert,
    service: ProductService = Depends(get_product_service)
):
    await service.insert(data)
    return {"status": "success", "message": "Urun eklendi"}

@router.delete("/delete", status_code=201)
async def delete_product(
    data: ProductDelete,
    service: ProductService = Depends(get_product_service)
):
    await service.delete(data)
    return {"status": "success", "message": "Urun silindi"}

@router.put("/update", status_code=201)
async def update_product(
    data: ProductUpdate,
    service: ProductService = Depends(get_product_service)
):
    await service.update(data)
    return {"status": "success", "message": "Urun güncellendi"}

@router.get("/select")
async def select_product(
    product_id: int,
    service: ProductService = Depends(get_product_service)
):
    return {"status": "success", "data": await service.get(product_id)}

@router.get("/select_all")
async def select_all_product(
    limit: int,
    offset: int,
    service: ProductService = Depends(get_product_service)
):
    return {"status": "success", "data": await service.get_all(limit, offset)}