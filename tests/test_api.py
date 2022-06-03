import pytest
from fastapi.testclient import TestClient

from shoppingcart.main import app


client = TestClient(app)

def test_can_get_empty_cart():
    response = client.get("/cart")
    assert response.status_code == 200
    assert response.json() == []


def test_can_add_product_to_cart():
    response = client.post("/cart", json={"product_id": "123", "quantity": 1, "price": 10})
    assert response.status_code == 200
    assert response.json() == {"product_id": "123", "quantity": 1, "price": 10, "purchaseble": True}
