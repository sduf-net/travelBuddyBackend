import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_sign_up_success():
    response = client.post("/auth/sign_up", json={
        "email": "newuser@example.com",
        "password": "Password123!",
        "password_confirm": "Password123!"
    })
    assert response.status_code == 200
    assert "token" in response.json()

def test_sign_in_success():
    client.post("/auth/sign_up", json={
        "email": "existinguser@example.com",
        "password": "Password123!",
        "password_confirm": "Password123!"
    })
    response = client.post("/auth/sign_in", json={
        "email": "existinguser@example.com",
        "password": "Password123!"
    })
    assert response.status_code == 200
    assert "token" in response.json()
