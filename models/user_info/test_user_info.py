from models.user_info.user_info import UserInfo


def test_user_info():
    user = UserInfo(user_id="user_id", email="email@email.com", password="password")

    assert str(user.user_id) == "user_id"
    assert str(user.email) == "email@email.com"
    assert user.hashed_password is not None

def test_with_personal_data():
    user = UserInfo(user_id="user_id", email="email@email.com", password="password")
    user_info = user.with_user_data(bio="bio", gender="gender", pictures=["pic1", "pic2"], geo={"key": "value"})

    assert str(user_info.user_id) == "user_id"
    assert str(user_info.bio) == "bio"
    assert str(user_info.gender) == "gender"
