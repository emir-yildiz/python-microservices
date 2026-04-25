from pydantic import BaseModel

class ProductInsert(BaseModel):
    product_id : int
    product_name : str
    updated_at: str

class ProductDelete(BaseModel):
    product_id: int

class ProductUpdate(BaseModel):
    product_id : int
    product_name : str
    updated_at: str
