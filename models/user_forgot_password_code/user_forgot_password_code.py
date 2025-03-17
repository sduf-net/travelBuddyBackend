import uuid
from sqlalchemy import Column, String, Index, ForeignKey, DateTime, func
from datetime import timedelta
from database import Base


class UserForgotPasswordCode(Base):
    __tablename__ = "user_forgot_password_code"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey('users.id'), nullable=False)
    code = Column(String, nullable=False, unique=True)
    expired_at = Column(DateTime, default=func.now(), nullable=False, index=True)
    created_at = Column(DateTime, default=func.now(), nullable=False)

    def __init__(self, user_id: str):
        self.id = str(uuid.uuid4())
        self.user_id = user_id
        self.code = str(uuid.uuid4().int)[:6]
        self.expired_at = func.now() + timedelta(minutes=10)