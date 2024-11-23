from models.user_info.user_info import UserInfo


def test_user_info():
    user = UserInfo(user_id="user_id", bio="bio", gender="gender",
                          pictures=["pic1", "pic2"], geo={"key": "value"})

    assert str(user.user_id) == "user_id"
    assert str(user.bio) == "bio"
    assert str(user.gender) == "gender"
    assert user.pictures == ["pic1", "pic2"]
    assert user.geo == {"key": "value"}
