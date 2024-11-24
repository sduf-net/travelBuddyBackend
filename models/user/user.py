import uuid
from sqlalchemy import Column, String, Boolean, DateTime, func
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    is_deleted = Column(Boolean, default=False)
    is_archived = Column(Boolean, default=False)
    created_at = Column(DateTime, default=func.now(), nullable=False)

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.is_deleted = False
        self.is_archived = False

    def archive(self):
        self.is_archived = True
        return self

    def delete(self):
        self.is_deleted = True
        return self