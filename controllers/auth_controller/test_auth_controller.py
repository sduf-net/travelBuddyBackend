import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_sign_up_success():
    response = client.post("/auth/sign_up", json={
        "payload": {
            "data": {
                "email": "newuser@example.com",
                "password": "Password123!",
                "password_confirm": "Password123!"
            }
        },
        "user_id": "user:travel:123",
        "screen_id": "12",
        "project_id": "project"
    })
    assert response.status_code == 200
    assert "token" in response.json()

def test_sign_in_success():
    client.post("/auth/sign_up", json={
        "payload": {
            "data": {
                "email": "existinguser@example.com",
                "password": "Password123!",
                "password_confirm": "Password123!"
            }
        },
        "user_id": "user:travel:123",
        "screen_id": "12",
        "project_id": "project"
    })
    response = client.post("/auth/sign_in", json={
        "payload": {
            "data": {
                "email": "existinguser@example.com",
                "password": "Password123!"
            }
        },
        "user_id": "user:travel:123",
        "screen_id": "12",
        "project_id": "project"
    })
    assert response.status_code == 200
    assert "token" in response.json()
