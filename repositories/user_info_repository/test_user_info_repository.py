import uuid
from sqlalchemy.orm import Session
from models.user.user import User
from models.user_info.user_info import UserInfo
from repositories.user_repository.user_repository import UserRepository
from repositories.user_info_repository.user_info_repository import UserInfoRepository


def test_save_user_info(db_session: Session):
    """Test saving a user to the database."""
    email = f"{uuid.uuid4()}@example.com"
    user = User()
    user_info = UserInfo(user_id=user.id, email=email, password="Password123!")

    user = UserRepository.save(db_session, user)
    user_info = UserInfoRepository.save(db_session, user_info)
    assert str(user_info.email) == email
    # Ensure password check works
    assert user_info.check_password("Password123!")


def test_get_user_by_id(db_session: Session):
    """Test retrieving a user by id."""
    # First, create a user in the database
    email = f"{uuid.uuid4()}@example.com"
    user = User()
    user_info = UserInfo(user_id=user.id, email=email, password="Password1!")

    UserRepository.save(db_session, user)
    saved_user_info = UserInfoRepository.save(db_session, user_info)
    # Now, retrieve the user by email
    user = UserInfoRepository.get_by_user_id(db_session, saved_user_info.user_id)
    assert user is not None
    assert str(user.email) == email
    assert str(user.id) == str(saved_user_info.id)
    assert str(user.user_id) == str(saved_user_info.user_id)


def test_get_by_email(db_session: Session):
    """Test retrieving a user by id."""
    # First, create a user in the database
    email = f"{uuid.uuid4()}@example.com"

    user = User()
    user_info = UserInfo(user_id=user.id, email=email, password="Password1!")

    UserRepository.save(db_session, user)
    saved_user_info = UserInfoRepository.save(db_session, user_info)
    # Now, retrieve the user by email
    user = UserInfoRepository.get_by_email(db_session, saved_user_info.email)
    assert user is not None
    assert str(user.email) == email
    assert str(user.id) == str(saved_user_info.id)
    assert str(user.user_id) == str(saved_user_info.user_id)
