from sqlalchemy.orm import Session
from repositories.user_repository.user_repository import UserRepository

def test_save_user(db_session: Session):
    """Test saving a user to the database."""
    user = UserRepository.save(db_session, email="testuser@example.com", password="Password123!")
    assert user.email == "testuser@example.com"
    assert user.check_password("Password123!")  # Ensure password check works

def test_get_user_by_email(db_session: Session):
    """Test retrieving a user by email."""
    # First, create a user in the database
    UserRepository.save(db_session, email="testuser1@example.com", password="Password123!")
    # Now, retrieve the user by email
    user = UserRepository.get_by_email(db_session, "testuser1@example.com")
    assert user is not None
    assert user.email == "testuser1@example.com"
