from http import HTTPStatus
import pytest
from fastapi.testclient import TestClient

from shoppingcart.main import app
from tools import fake_cart
from tools.schemas import ProductRequest

client = TestClient(app)


@pytest.fixture
def request_payload():
    return ProductRequest(sku="123", quantity=1, price=10)


@pytest.fixture(autouse=True)
def clean_cart():
    fake_cart.flush()


def test_can_get_empty_cart():
    response = client.get("/cart")

    assert response.status_code == HTTPStatus.OK


def test_can_add_product_to_cart_and_retrieve_it(request_payload):
    client.put("/cart", request_payload.json())

    response = client.get("/cart")

    assert response.status_code == HTTPStatus.OK


def test_can_add_product_to_cart(request_payload):
    response = client.put("/cart", request_payload.json())

    assert response.status_code == HTTPStatus.OK


def test_cannot_add_product_to_cart_when_bad_request():
    response = client.put("/cart", json={"sku": "123", "quantity": "a", "price": 10})

    assert response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY


def test_can_update_product_in_cart(request_payload):
    client.put("/cart", request_payload.json())

    update_request = ProductRequest(sku=request_payload.sku, quantity=2, price=request_payload.price)

    response = client.put("/cart", json=update_request.dict())

    assert response.status_code == HTTPStatus.OK


def test_can_delete_product_from_cart(request_payload):
    client.put("/cart", request_payload.json())

    response = client.delete(f"/cart/product/{request_payload.sku}")

    assert response.status_code == HTTPStatus.OK


def test_cannot_delete_discount_from_cart_if_not_found():
    response = client.delete("/cart/product/random-code")

    assert response.status_code == HTTPStatus.NOT_MODIFIED


def test_cannot_delete_product_from_cart_if_not_found():
    response = client.delete("/cart/product/random-sku-code")

    assert response.status_code == HTTPStatus.NOT_MODIFIED


def test_can_delete_all_products_from_cart(request_payload):
    client.put("/cart", request_payload.json())

    response = client.delete("/cart")

    assert response.status_code == HTTPStatus.OK


def test_can_add_discount_to_cart(request_payload):
    client.put("/cart", request_payload.json())

    response = client.post("/cart/discount", json={"code": "10OFF"})

    assert response.status_code == HTTPStatus.OK


def test_cannot_add_discount_that_does_not_exist(request_payload):
    client.put("/cart", request_payload.json())

    response = client.post("/cart/discount", json={"code": "RANDOM-DISCOUNT"})

    assert response.status_code == HTTPStatus.NOT_FOUND
    

def test_cannot_add_disabled_discount(request_payload):
    client.put("/cart", request_payload.json())

    response = client.post("/cart/discount", json={"code": "30OFF"})

    assert response.status_code == HTTPStatus.BAD_REQUEST