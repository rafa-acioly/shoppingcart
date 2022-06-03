from pydantic import BaseModel
from decimal import Decimal


class Product(BaseModel):
    product_id: str
    quantity: int
    price: Decimal
