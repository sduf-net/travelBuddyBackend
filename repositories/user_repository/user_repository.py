from sqlalchemy.orm import Session
from models.user.user import User


class UserRepository:
    @staticmethod
    def save(session: Session, user: User):
        session.add(user)
        session.commit()
        return user

    @staticmethod
    def get_by_email(session: Session, email: str):
        return session.query(User).filter(User.email == email).first()
