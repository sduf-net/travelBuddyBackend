import uuid
from sqlalchemy.orm import Session
from repositories.user_repository.user_repository import UserRepository
from models.user.user import User


def test_save_user(db_session: Session):
    """Test saving a user to the database."""
    email = f"{uuid.uuid4()}@example.com"
    user = User(email=email, password="Password123!")
    user = UserRepository.save(db_session, user)
    assert str(user.email) == email
    assert user.check_password("Password123!")  # Ensure password check works


def test_get_user_by_email(db_session: Session):
    """Test retrieving a user by email."""
    # First, create a user in the database
    email = f"{uuid.uuid4()}@example.com"
    user = User(email=email, password="Password123!")
    UserRepository.save(db_session, user)
    # Now, retrieve the user by email
    user = UserRepository.get_by_email(db_session, email)
    assert user is not None
    assert str(user.email) == email

def test_get_user_by_id(db_session: Session):
    """Test retrieving a user by id."""
    # First, create a user in the database
    email = f"{uuid.uuid4()}@example.com"
    user = User(email=email, password="Password123!")
    saved_user = UserRepository.save(db_session, user)
    # Now, retrieve the user by email
    user = UserRepository.get_by_id(db_session, saved_user.id)
    assert user is not None
    assert str(user.email) == email
    assert str(user.id) == str(saved_user.id)
