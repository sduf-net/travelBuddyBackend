import uuid
from models.user_forgot_password_code.user_forgot_password_code import UserForgotPasswordCode
from datetime import datetime
from datetime import datetime, timedelta

def test_create_new_code():
    user_id = str(uuid.uuid4())
    user_forgot_password_code = UserForgotPasswordCode(user_id=user_id)

    assert user_forgot_password_code.user_id == user_id
    # assert user_forgot_password_code.expired_at > datetime.now()
    # assert user_forgot_password_code.expired_at < datetime.now() + timedelta(minutes=11)
    assert user_forgot_password_code.code is not None

def test_code_length():
    user_id = str(uuid.uuid4())
    user_forgot_password_code = UserForgotPasswordCode(user_id=user_id)

    assert len(user_forgot_password_code.code) == 6

def test_unique_code():
    user_id = str(uuid.uuid4())
    user_forgot_password_code1 = UserForgotPasswordCode(user_id=user_id)
    user_forgot_password_code2 = UserForgotPasswordCode(user_id=user_id)

    assert user_forgot_password_code1.code != user_forgot_password_code2.code