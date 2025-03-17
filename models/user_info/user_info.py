import uuid
import bcrypt
from sqlalchemy import Column, String, ForeignKey, Text, Boolean
from sqlalchemy.dialects.postgresql import ARRAY, JSON
from database import Base


class UserInfo(Base):
    __tablename__ = "user_info"

    user_id = Column(String, ForeignKey('users.id'), primary_key=True, nullable=False, unique=True)
    email = Column(String, unique=True, nullable=False)
    email_verified = Column(Boolean, default=False)
    hashed_password = Column(String, nullable=False)

    def __init__(self, user_id: str, email: str, password: str):
        hashed_password = bcrypt.hashpw(
            password.encode(), bcrypt.gensalt()).decode()
        self.user_id = user_id
        self.email = email
        self.email_verified = False
        self.hashed_password = hashed_password

    def set_email_verified(self):
        self.email_verified = True
        return self

    def check_password(self, password: str) -> bool:
        return bcrypt.checkpw(password.encode(), self.hashed_password.encode())
