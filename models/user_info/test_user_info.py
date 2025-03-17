from models.user_info.user_info import UserInfo


def test_user_info():
    user = UserInfo(user_id="user_id", email="email@email.com", password="password")

    assert str(user.user_id) == "user_id"
    assert str(user.email) == "email@email.com"
    assert user.hashed_password is not None

def test_with_full_name():
    user = UserInfo(user_id="user_id", email="email@email.com", password="password")

    new_user = UserInfo.with_full_name(user, "new_full_name")
    assert str(new_user.full_name) == "new_full_name"

def test_with_phone():
    user = UserInfo(user_id="user_id", email="email@email.com", password="password")

    new_user = UserInfo.with_phone(user, "123123123")
    assert str(new_user.phone) == "123123123"

def test_set_email_verified():
    user = UserInfo(user_id="user_id", email="email@email.com", password="password")
    assert user.email_verified == False

    new_user = UserInfo.set_email_verified(user)
    assert new_user.email_verified == True

