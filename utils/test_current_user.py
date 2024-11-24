from sqlalchemy.orm import Session
from utils.current_user import get_current_user, TokenRequest
from utils.token import Token
from models.user.user import User
from models.user_info.user_info import UserInfo
from repositories.user_repository.user_repository import UserRepository
from repositories.user_info_repository.user_info_repository import UserInfoRepository

def test_get_current_user(db_session: Session):
    user = User()
    user = UserRepository.save(db_session, user)

    token=Token.generate_and_sign(user_id=user.id)
    params = TokenRequest(user_token=token)

    current_user = get_current_user(params, db_session)

    assert current_user.id == user.id
