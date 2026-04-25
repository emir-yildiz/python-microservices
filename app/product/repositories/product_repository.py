import asyncpg
from schemas import ProductInsert, ProductDelete, ProductUpdate


class ProductRepository:
    def __init__(self, db_pool: asyncpg.Pool):
        self._pool = db_pool

    async def exists(self, product_id: int) -> bool:
        async with self._pool.acquire() as conn:
            return await conn.fetchval(
                "SELECT product_id FROM microservice.products WHERE product_id = $1",
                product_id
            ) is not None

    async def insert(self, data: ProductInsert) -> None:
        async with self._pool.acquire() as conn:
            async with conn.transaction():
                await conn.execute("""
                    INSERT INTO microservice.products (product_id, product_name, updated_at)
                    VALUES ($1, $2, to_date($3, 'YYYYMMDD'))
                    ON CONFLICT (product_id) DO NOTHING;
                """, data.product_id, data.product_name, data.updated_at)
                #     ^^^ removed trailing comma — it was silently discarding the awaited result

    async def delete(self, product_id: int) -> None:  # ← was accepting ProductDelete, but service passes a plain int
        async with self._pool.acquire() as conn:
            async with conn.transaction():
                await conn.execute("""
                    DELETE FROM microservice.products
                    WHERE product_id = $1;
                """, product_id)  # ← was data.product_id

    async def update(self, data: ProductUpdate) -> None:
        async with self._pool.acquire() as conn:
            async with conn.transaction():
                await conn.execute("""
                    UPDATE microservice.products
                    SET product_name = $2, updated_at = to_date($3,'YYYYMMDD')
                    WHERE product_id = $1;
                """, data.product_id, data.product_name, data.updated_at)

    async def find_by_id(self, product_id: int):
        async with self._pool.acquire() as conn:
            return await conn.fetchrow(
                "SELECT * FROM microservice.products WHERE product_id = $1",  # ← was only selecting product_id
                product_id
            )

    async def find_all(self, limit: int, offset: int):
        async with self._pool.acquire() as conn:
            return await conn.fetch(
                "SELECT * FROM microservice.products ORDER BY product_id LIMIT $1 OFFSET $2",  # ← typo: productid → product_id
                limit, offset
            )