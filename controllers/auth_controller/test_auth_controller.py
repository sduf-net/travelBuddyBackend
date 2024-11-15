def test_sign_in_success(client):
    response = client.post("/auth/sign_up", json={
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
    assert response.status_code == 204


def test_sign_in_missing_email(client):
    response = client.post("/auth/sign_in", json={
        "payload": {
            "data": {
                "password": "Password123!"
            }
        },
        "user_id": "user:travel:123",
        "screen_id": "12",
        "project_id": "project"
    })
    print(response)
    assert response.status_code == 200
    response_json = response.json()
    assert "error_message" in response_json
    assert response_json["error_message"] == "Missing required fields (email, password)"


def test_sign_in_invalid_email_format(client):
    response = client.post("/auth/sign_in", json={
        "payload": {
            "data": {
                "email": "invalid-email-format",
                "password": "Password123!"
            }
        },
        "user_id": "user:travel:123",
        "screen_id": "12",
        "project_id": "project"
    })
    assert response.status_code == 204
    response_json = response.json()
    assert "error_message" in response_json
    assert response_json["error_message"] == "Invalid email format"


def test_sign_in_incorrect_credentials(client):
    # Sign up a user first
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
    
    # Test sign-in with incorrect password
    response = client.post("/auth/sign_in", json={
        "payload": {
            "data": {
                "email": "newuser@example.com",
                "password": "WrongPassword!"
            }
        },
        "user_id": "user:travel:123",
        "screen_id": "12",
        "project_id": "project"
    })
    assert response.status_code == 204
    response_json = response.json()
    assert "error_message" in response_json
    assert response_json["error_message"] == "Incorrect email or password"


# Test cases for sign_up route
def test_sign_up_success(client):
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
    assert response.status_code == 204


def test_sign_up_passwords_do_not_match(client):
    response = client.post("/auth/sign_up", json={
        "payload": {
            "data": {
                "email": "newuser@example.com",
                "password": "Password123!",
                "password_confirm": "DifferentPassword123!"
            }
        },
        "user_id": "user:travel:123",
        "screen_id": "12",
        "project_id": "project"
    })
    assert response.status_code == 204
    response_json = response.json()
    assert "error_message" in response_json
    assert response_json["error_message"] == "Passwords do not match"


def test_sign_up_user_already_registered(client):
    # Sign up a user first
    response = client.post("/auth/sign_up", json={
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
    
    # Try to sign up with the same email again
    response = client.post("/auth/sign_up", json={
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
    assert response.status_code == 204
    response_json = response.json()
    assert "error_message" in response_json
    assert response_json["error_message"] == "User already registered"
