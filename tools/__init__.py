from decimal import Decimal
from shoppingcart.entities import Product

fake_products = [
    Product(product_id="1", quantity=1, price=Decimal("10.00")),
    Product(product_id="2", quantity=2, price=Decimal("20.00")),
    Product(product_id="3", quantity=3, price=Decimal("30.00")),
    Product(product_id="4", quantity=4, price=Decimal("40.00")),
    Product(product_id="5", quantity=5, price=Decimal("50.00")),
]
