from sqlalchemy.orm import Session
from repositories.user_repository.user_repository import UserRepository
import uuid

def test_save_user(db_session: Session):
    """Test saving a user to the database."""
    email=f"{uuid.uuid4()}@example.com"
    user = UserRepository.save(db_session, email=email, password="Password123!")
    assert user.email == email
    assert user.check_password("Password123!")  # Ensure password check works

def test_get_user_by_email(db_session: Session):
    """Test retrieving a user by email."""
    # First, create a user in the database
    email=f"{uuid.uuid4()}@example.com"
    UserRepository.save(db_session, email=email, password="Password123!")
    # Now, retrieve the user by email
    user = UserRepository.get_by_email(db_session, email)
    assert user is not None
    assert user.email == email
