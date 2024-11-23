from models.user.user import User

def test_create_user():
    user = User(email="testuser@example.com", password="password123")

    assert str(user.email) == "testuser@example.com"
    assert user.hashed_password is not None

def test_set_email_verified():
    user = User(email="testuser@example.com", password="password123")
    user = user.set_email_verified()

    assert bool(user.email_verified) is True

def test_check_password():
    user = User(email="testuser@example.com", password="password123")

    assert user.check_password("password123") is True
    assert user.check_password("invalid") is False
