from http import HTTPStatus

from fastapi import FastAPI, HTTPException, Path

from tools import fake_cart as cart_service
from tools import fake_discounts as discount_service
from tools.schemas import Cart, DiscountRequest, ProductRequest

app = FastAPI()


@app.get("/cart", response_model=Cart)
async def index() -> Cart:
    """List all products that were add to the cart."""
    return cart_service


@app.put("/cart", response_model=Cart)
async def upsert(product: ProductRequest) -> Cart:
    """Update a product on the cart."""
    cart_service.upsert_product(product)
    return cart_service


@app.delete("/cart", status_code=HTTPStatus.OK)
async def flush() -> None:
    """Remove all products from the cart."""
    cart_service.flush()


@app.delete("/cart/product/{product_sku}", status_code=HTTPStatus.OK)
async def delete(
    product_sku: str = Path(description="Unique identifier of the product to delete from the cart")  # noqa: E501
) -> None:
    """Remove a product from the cart."""
    if not cart_service.remove_product(product_sku):
        raise HTTPException(
            status_code=HTTPStatus.NOT_MODIFIED,
            detail=f"Product with sku: {product_sku} not found on the cart."
        )



@app.post("/cart/discount", response_model=Cart)
async def add_discount(requested_discount: DiscountRequest) -> Cart:
    """Add a discount to the cart."""
    discount = [coupon for coupon in discount_service if coupon.code == requested_discount.code]  # noqa: E501
    if not discount:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail=f"Discount with code: {requested_discount.code} not found."
        )

    discount_founded = discount[0]
    if not discount_founded.enabled:
        raise HTTPException(
            status_code=HTTPStatus.BAD_REQUEST,
            detail=f"Discount with code: {requested_discount.code} is disabled."
        )

    cart_service.add_discount(discount_founded)
    return cart_service
