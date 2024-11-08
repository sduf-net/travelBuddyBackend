import pytest
from sqlalchemy.orm import Session
from database import get_db
from repositories.user_repository.user_repository import UserRepository

def test_save_user():
    db: Session = next(get_db())
    user = UserRepository.save(db, email="testuser@example.com", password="Password123!")
    assert user.email == "testuser@example.com"
    assert user.check_password("Password123!")

def test_get_user_by_email():
    db: Session = next(get_db())
    user = UserRepository.get_by_email(db, "testuser@example.com")
    assert user is not None
    assert user.email == "testuser@example.com"
