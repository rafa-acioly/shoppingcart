from pydantic import BaseModel, Field

import uuid
from typing import List
from pydantic import BaseModel
from decimal import Decimal


class Discount(BaseModel):
    code: str


class ProductRequest(BaseModel):
    sku: str
    quantity: int = Field(gt=1)
    price: Decimal = Field(gt=Decimal("0.00"))


class Cart(BaseModel):
    id: str = Field(default_factory=lambda: str(uuid.uuid4()))
    products: List[ProductRequest]
    discounts: List[Discount] = []
    total: Decimal = Field(default=Decimal("0.00"), decimal_places=2)
    subtotal: Decimal = Field(default=Decimal("0.00"), decimal_places=2)

    def refresh_total(self):
        self.total = Decimal(sum(
            product.price * product.quantity
            for product in self.products
        ))
        self.refresh_subtotal()
    
    def refresh_subtotal(self):
        self.subtotal = self.total - sum(
            discount.amount
            for discount in self.discounts
        )

        if self.subtotal < 0:
            self.subtotal = Decimal("0.00")
    
    def upsert_product(self, product: ProductRequest):
        for product_ in self.products:
            if product_.sku == product.sku:
                product_.quantity = product.quantity
                self.refresh_total()
                return

        self.add_product(product)
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