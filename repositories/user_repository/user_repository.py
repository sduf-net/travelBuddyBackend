from sqlalchemy.orm import Session
from models.user import User
import bcrypt

class UserRepository:
    @staticmethod
    def save(session: Session, email: str, password: str):
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        user = User(email=email, hashed_password=hashed_password)
        session.add(user)
        session.commit()
        return user

    @staticmethod
    def get_by_email(session: Session, email: str):
        print(session)
        return session.query(User).filter(User.email == email).first()
