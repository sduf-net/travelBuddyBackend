import uuid
import bcrypt
from sqlalchemy import Column, String, ForeignKey, Text, Boolean
from sqlalchemy.dialects.postgresql import ARRAY, JSON
from database import Base


class UserInfo(Base):
    __tablename__ = "user_info"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey('users.id'), nullable=False, unique=True)
    email = Column(String, unique=True, nullable=False)
    email_verified = Column(Boolean, default=False)
    hashed_password = Column(String, nullable=False)
    bio = Column(Text, nullable=True)
    gender = Column(String, nullable=True)
    pictures = Column(ARRAY(String), nullable=True)
    geo = Column(JSON, nullable=True)

    def __init__(self, user_id: str, email: str, password: str):
        hashed_password = bcrypt.hashpw(
            password.encode(), bcrypt.gensalt()).decode()
        self.user_id = user_id
        self.email = email
        self.hashed_password = hashed_password

    def with_user_data(self, bio: str, gender: str, pictures: list | None = None, geo: dict | None = None):
        self.bio = bio
        self.gender = gender
        self.pictures = pictures
        self.geo = geo
        return self

    def with_pictures(self, pictures: list | None = None):
        self.pictures = pictures
        return self

    def with_geo(self, geo: dict | None = None):
        self.geo = geo
        return self

    def set_email_verified(self):
        self.email_verified = True
        return self

    def check_password(self, password: str) -> bool:
        return bcrypt.checkpw(password.encode(), self.hashed_password.encode())
