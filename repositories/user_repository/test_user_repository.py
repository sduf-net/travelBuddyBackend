from sqlalchemy.orm import Session
from repositories.user_repository.user_repository import UserRepository
from models.user.user import User


def test_save_user(db_session: Session):
    """Test saving a user to the database."""
    user = User()
    user = UserRepository.save(db_session, user)
    assert user.id is not None

def test_get_user_by_id(db_session: Session):
    """Test retrieving a user by id."""
    # First, create a user in the database
    user = User()
    saved_user = UserRepository.save(db_session, user)
    # Now, retrieve the user by email
    user = UserRepository.get_by_id(db_session, saved_user.id)
    assert user is not None
    assert str(user.id) == str(saved_user.id)
