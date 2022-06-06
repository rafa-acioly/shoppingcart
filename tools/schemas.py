from pydantic import BaseModel, Field


from typing import List
from pydantic import BaseModel
from decimal import Decimal


class Discount(BaseModel):
    discount_id: str
    discount_value: Decimal


class ProductRequest(BaseModel):
    sku: str
    quantity: int
    price: Decimal


class Cart(BaseModel):
    products: List[ProductRequest]
    discounts: List[Discount] = []
    subtotal: Decimal = Field(default=Decimal("0"), decimal_places=2)


    def refresh_subtotal(self):
        self.subtotal = Decimal(sum(
            product.price * product.quantity
            for product in self.products
        ))
    
    def add_product(self, product: ProductRequest):
        self.products.append(product)
        self.refresh_subtotal()

    def contains(self, sku: str):
        for product in self.products:
            if product.sku == sku:
                return True
        return False

    def remove_product(self, sku: str):
        for product in self.products:
            if product.sku == sku:
                self.products.remove(product)
                self.refresh_subtotal()