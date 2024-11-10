from sqlalchemy.orm import Session
from conftest import client
from utils.current_user import get_current_user, TokenRequest
from schemas.auth.token import Token
from repositories.user_repository.user_repository import UserRepository

def test_get_current_user(db_session: Session):
    user = UserRepository.save(db_session, email="test@test.com", password="Password1!")
    token=Token.generate_and_sign(user_id=user.id)
    params = TokenRequest(user_token=token)

    current_user = get_current_user(params, db_session)

    assert current_user.id == user.id
