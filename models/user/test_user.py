from models.user.user import User

def test_create_user():
    user = User()

    assert user.id is not None