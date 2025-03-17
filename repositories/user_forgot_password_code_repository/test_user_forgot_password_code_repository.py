import uuid
from sqlalchemy.orm import Session
from models.user.user import User
from repositories.user_repository.user_repository import UserRepository
from models.user_forgot_password_code.user_forgot_password_code import UserForgotPasswordCode
from repositories.user_forgot_password_code_repository.user_forgot_password_code_repository import UserForgotPasswordCodeRepository


def test_save_user_forgot_password_code(db_session: Session):
    user = User()
    user = UserRepository.save(db_session, user)

    user_forgot_password_code = UserForgotPasswordCode(user_id=user.id)
    user_forgot_password_code = UserForgotPasswordCodeRepository.save(db_session, user_forgot_password_code)

    assert str(user_forgot_password_code.user_id) == user.id
    assert user_forgot_password_code.code is not None


def test_validate_code(db_session: Session):
    user = User()
    user = UserRepository.save(db_session, user)

    user_forgot_password_code = UserForgotPasswordCode(user_id=user.id)
    user_forgot_password_code = UserForgotPasswordCodeRepository.save(db_session, user_forgot_password_code)

    is_valid = UserForgotPasswordCodeRepository.validate_code(db_session, user_id=user.id, code=user_forgot_password_code.code)
    assert is_valid is True

    is_valid = UserForgotPasswordCodeRepository.validate_code(db_session, user_id=str(uuid.uuid4()), code=user_forgot_password_code.code)
    assert is_valid is False

    is_valid = UserForgotPasswordCodeRepository.validate_code(db_session, user_id=user.id, code="123456")
    assert is_valid is False

def test_get_valid_code(db_session: Session):
    user = User()
    user = UserRepository.save(db_session, user)

    user_forgot_password_code = UserForgotPasswordCode(user_id=user.id)
    user_forgot_password_code = UserForgotPasswordCodeRepository.save(db_session, user_forgot_password_code)

    user_code = UserForgotPasswordCodeRepository.get_valid_code(db_session, code=user_forgot_password_code.code)
    assert user_code.user_id == user.id
    assert user_code.code is not None

    user_code = UserForgotPasswordCodeRepository.get_valid_code(db_session, code="123456")
    assert user_code is None