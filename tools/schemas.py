from gc import enable
from pydantic import BaseModel, Field, PositiveInt, condecimal

import uuid
from typing import List
from pydantic import BaseModel
from decimal import Decimal


class DiscountRequest(BaseModel):
    code: str

class Discount(BaseModel):
    code: str
    amount: Decimal = Field(default=Decimal("0.00"))
    enabled: bool = True


class ProductRequest(BaseModel):
    sku: str
    quantity: int = Field(gt=0)
    price: float = Field(gt=0)


class Cart(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    products: List[ProductRequest]
    discounts: List[Discount] = []
    total: Decimal = Field(default=Decimal("0.00"))
    subtotal: Decimal = Field(default=Decimal("0.00"))

    def refresh_total(self):
        self.total = Decimal(sum(
            product.price * product.quantity
            for product in self.products
        ))
        self.refresh_subtotal()
    
    def refresh_subtotal(self):
        self.subtotal = self.total - Decimal(sum(
            discount.amount
            for discount in self.discounts
        ))

        if self.subtotal < 0:
            self.subtotal = Decimal("0.00")
    
    def upsert_product(self, product: ProductRequest):
        for product_ in self.products:
            if product_.sku == product.sku:
                product_.quantity = product.quantity
                self.refresh_total()
                return

        self.products.append(product)
        self.refresh_total()

    def add_discount(self, discount: Discount):
        self.discounts.append(discount)
        self.refresh_subtotal()

    def remove_product(self, sku: str):
        for product in self.products:
            if product.sku == sku:
                self.products.remove(product)
                self.refresh_total()
                return True
        
        return False
    
    def flush(self):
        self.products = []
        self.discounts = []
        self.total = Decimal("0.00")
        self.subtotal = Decimal("0.00")