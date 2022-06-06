from decimal import Decimal
from tools.schemas import Cart, ProductRequest, Discount


def test_can_add_product():
    cart = Cart(products=[])
    product = ProductRequest(sku="123", quantity=1, price=10)
    cart.upsert_product(product)

    assert len(cart.products) == 1


def test_can_calculate_total():
    cart = Cart(products=[])
    product = ProductRequest(sku="123", quantity=1, price=10)
    cart.upsert_product(product)

    assert cart.total == product.price * product.quantity


def test_cannot_add_duplicated_products():
    cart = Cart(products=[])
    product = ProductRequest(sku="123", quantity=1, price=10)

    cart.upsert_product(product)
    cart.upsert_product(product)

    assert len(cart.products) == 1


def test_can_update_product():
    cart = Cart(products=[])
    product = ProductRequest(sku="123", quantity=1, price=10)
    cart.upsert_product(product)

    product = ProductRequest(sku="123", quantity=2, price=10)
    cart.upsert_product(product)

    assert len(cart.products) == 1
    assert cart.products[0].quantity == 2


def test_can_calc_subtotal():
    cart = Cart(products=[])
    product = ProductRequest(sku="123", quantity=1, price=10)
    cart.upsert_product(product)

    expected = product.price * product.quantity
    cart.refresh_total()

    assert expected == cart.total


def test_can_calc_subtotal_with_discount():
    cart = Cart(products=[])
    product = ProductRequest(sku="123", quantity=1, price=10)
    cart.upsert_product(product)

    discount = Discount(code="10OFF", amount=Decimal("10"), enabled=True)
    cart.add_discount(discount)

    expected = Decimal(product.price * product.quantity) - discount.amount

    assert Decimal(expected) == cart.subtotal


def test_cannot_reach_negative_subtotal():
    cart = Cart(products=[])
    product = ProductRequest(sku="123", quantity=1, price=10)
    cart.upsert_product(product)

    discount = Discount(code="10OFF", amount=Decimal("10"), enabled=True)
    cart.add_discount(discount)

    discount = Discount(code="20OFF", amount=Decimal("20"), enabled=True)
    cart.add_discount(discount)

    assert cart.subtotal == 0
