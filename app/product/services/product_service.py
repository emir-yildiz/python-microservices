from repositories.product_repository import ProductRepository
from schemas import ProductUpdate, ProductDelete, ProductInsert
from exceptions.product_exception import ProductAlreadyExistsException, ProductNotFoundException  # ← eksikti


class ProductService:
    def __init__(self, repo: ProductRepository):
        self._repo = repo

    async def insert(self, data: ProductInsert):
        if await self._repo.exists(data.product_id):
            raise ProductAlreadyExistsException(f"Urun zaten mevcut: {data.product_id}")
        await self._repo.insert(data)

    async def update(self, data: ProductUpdate):
        if not await self._repo.exists(data.product_id):  # ← mantık hatası: insert gibi yazılmış, "not" eksikti
            raise ProductNotFoundException(f"Urun bulunamadi: {data.product_id}")
        await self._repo.update(data)

    async def delete(self, data: ProductDelete):
        if not await self._repo.exists(data.product_id):  # ← product_id → data.product_id
            raise ProductNotFoundException(f"Urun bulunamadi: {data.product_id}")
        await self._repo.delete(data.product_id)  # ← product_id → data.product_id

    async def get(self, product_id: int):
        row = await self._repo.find_by_id(product_id)
        if not row:
            raise ProductNotFoundException(f"Urun bulunamadi: {product_id}")
        return dict(row)

    async def get_all(self, limit: int, offset: int):
        rows = await self._repo.find_all(limit, offset)
        if not rows:
            raise ProductNotFoundException("Hic urun bulunamadi")  # ← product_id burada tanımsız değişkendi
        return [dict(row) for row in rows]  # ← dict([...]) yanlış, liste comprehension olmalı