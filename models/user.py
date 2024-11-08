from sqlalchemy import Column, String, Boolean
import uuid
import bcrypt
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String, unique=True, nullable=False)
    email_verified = Column(Boolean, default=False)
    hashed_password = Column(String, nullable=False)

    def check_password(self, password: str) -> bool:
        return bcrypt.checkpw(password.encode(), self.hashed_password.encode())
