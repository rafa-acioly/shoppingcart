from pydantic import BaseModel
from decimal import Decimal


class ProductRequest(BaseModel):
    product_id: str
    quantity: int
    price: Decimal


class ProductResponse(ProductRequest):
    purchaseble: bool = True
