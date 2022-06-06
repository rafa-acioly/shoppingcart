from typing import List
from fastapi import FastAPI, HTTPException, Path
from http import HTTPStatus

from tools import fake_cart
from tools.schemas import ProductRequest, Response

app = FastAPI()


@app.get("/cart", response_model=Response)
async def index() -> Response:
    """List all products that were add to the cart."""
    return fake_cart


@app.post("/cart", response_model=Response)
async def save(product: ProductRequest) -> Response:
    """Adds a new product to the cart."""
    fake_cart.add_product(product)
    return fake_cart


@app.patch("/cart/{product_sku}")
async def update(
    product_cart: ProductRequest,
    product_sku: str = Path(description="Unique identifier of the product to update"),
) -> Response:
    """Update a product on the cart."""
    pass


@app.delete("/cart/{product_sku}", status_code=HTTPStatus.OK)
async def delete(
    product_sku: str = Path(description="Unique identifier of the product to delete from the cart")  # noqa: E501
) -> None:
    """Remove a product from the cart."""
    if not fake_cart.contains(product_sku):
        raise HTTPException(
            status_code=HTTPStatus.NOT_MODIFIED,
            detail=f"Product with sku: {product_sku} not found on the cart."
        )

    fake_cart.remove_product(product_sku)
