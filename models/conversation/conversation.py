import uuid
from sqlalchemy import Column, String, ForeignKey, Boolean, DateTime, func
from sqlalchemy.orm import relationship
from database import Base

class Conversation(Base):
    __tablename__ = 'conversations'

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey(
        'users.id', ondelete='CASCADE'), nullable=False)
    opponent_user_id = Column(String, ForeignKey(
        'users.id', ondelete='CASCADE'), nullable=False)
    is_archived = Column(Boolean, default=False)
    created_at = Column(DateTime, server_default=func.now())

    def __init__(self, user_id: str, opponent_user_id: str):
        self.user_id = user_id
        self.opponent_user_id = opponent_user_id

    def archive_conversation(self):
        self.is_archived = True
        return self
