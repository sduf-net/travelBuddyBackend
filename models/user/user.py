from sqlalchemy import Column, String, Boolean, DateTime, func
import uuid
import bcrypt
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String, unique=True, nullable=False)
    email_verified = Column(Boolean, default=False)
    hashed_password = Column(String, nullable=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)

    def __init__(self, email: str, password: str):
        hashed_password = bcrypt.hashpw(
            password.encode(), bcrypt.gensalt()).decode()
        self.email = email
        self.hashed_password = hashed_password

    def check_password(self, password: str) -> bool:
        return bcrypt.checkpw(password.encode(), self.hashed_password.encode())

    def set_email_verified(self):
        self.email_verified = True
        return self
