from decimal import Decimal
from tools.schemas import Cart, Discount


fake_cart = Cart(products=[])

fake_discounts = [
    Discount(code="10OFF", amount=Decimal("10.00")),
    Discount(code="20OFF", amount=Decimal("20.00")),
    Discount(code="30OFF", amount=Decimal("30.00")),
]