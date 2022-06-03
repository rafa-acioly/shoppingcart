from typing import List
from shoppingcart.entities import ProductRequest


"""
fake_products will hold the list of products that were added to the cart.

Maybe it would be better to use a hashmap instead of a list,
so that we can retrieve the product by its id faster, O(1) instead of O(n).
Example:
    {
        "123:": {
            "product_id": "123",
            "quantity": 1,
            "price": Decimal("10.00"),
            "purchasble": True
        },
        "456": {
            "product_id": "456",
            "quantity": 2,
            "price": Decimal("20.00"),
            "purchasble": True
        }
    }
"""
fake_products: List[ProductRequest] = []
