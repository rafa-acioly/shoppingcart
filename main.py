from typing import List
from fastapi import FastAPI

from shoppingcart.entities import Product

app = FastAPI()


@app.get("/cart", response_model=List[Product])
async def index() -> List[Product]:
    """List all products that were add to the cart."""
    pass


@app.post("/cart")
async def create(product: Product) -> Product:
    """Adds a new product to the cart."""
    pass


@app.patch("/cart/{cart_id}")
async def update(cart_id: str, product_cart: Product) -> Product:
    """Update a product on the cart."""
    pass


@app.delete("/cart/{product_id}")
async def delete(product_id: str):
    """Remove a product from the cart."""
    pass
