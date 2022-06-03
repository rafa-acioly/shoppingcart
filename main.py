from typing import List
from fastapi import FastAPI

from shoppingcart.entities import Product
from tools import fake_products

app = FastAPI()


@app.get("/cart", response_model=List[Product])
async def index() -> List[Product]:
    """List all products that were add to the cart."""
    return fake_products


@app.post("/cart")
async def create(product: Product) -> Product:
    """Adds a new product to the cart."""
    fake_products.append(product)
    return product


@app.patch("/cart/{product_id}")
async def update(product_id: str, product_cart: Product) -> Product:
    """Update a product on the cart."""
    pass


@app.delete("/cart/{product_id}")
async def delete(product_id: str):
    """Remove a product from the cart."""
    pass
