from typing import List
from fastapi import FastAPI

from shoppingcart.entities import ProductRequest, ProductResponse
from tools import fake_products

app = FastAPI()


@app.get("/cart", response_model=List[ProductRequest])
async def index() -> List[ProductResponse]:
    """List all products that were add to the cart."""
    return fake_products


@app.post("/cart", response_model=ProductResponse)
async def create(product: ProductRequest) -> ProductResponse:
    """Adds a new product to the cart."""
    fake_products.append(product)
    return product


@app.patch("/cart/{product_id}")
async def update(
    product_id: str,
    product_cart: ProductRequest
) -> ProductRequest:
    """Update a product on the cart."""
    pass


@app.delete("/cart/{product_id}")
async def delete(product_id: str):
    """Remove a product from the cart."""
    pass