from sqlalchemy.orm import Session
from models.user import User
import bcrypt
import re

class UserRepository:
    @staticmethod
    def save(session: Session, email: str, password: str):
        if not re.match(r".+@.+\..+", email):
            raise ValueError("Email is invalid")
        if len(password) < 8 or not any(char.isdigit() for char in password) \
                or not any(char.isupper() for char in password) or not any(char.islower() for char in password) \
                or not re.search(r"[#?!@$%^&*()]", password):
            raise ValueError("Password does not meet requirements")
        
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        user = User(email=email, hashed_password=hashed_password)
        session.add(user)
        session.commit()
        return user

    @staticmethod
    def get_by_email(session: Session, email: str):
        print(session)
        return session.query(User).filter(User.email == email).first()
