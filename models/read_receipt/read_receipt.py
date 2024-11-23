import uuid
from sqlalchemy import Column, String, ForeignKey, DateTime, func
from sqlalchemy.orm import relationship
from database import Base


class ReadReceipt(Base):
    __tablename__ = 'read_receipts'

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    conversation_id = Column(String, ForeignKey(
        'conversations.id', ondelete='CASCADE'), nullable=False)
    user_id = Column(String, ForeignKey(
        'users.id', ondelete='CASCADE'), nullable=False)
    last_read_message_id = Column(String, ForeignKey(
        'messages.id', ondelete='CASCADE'), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(),
                        onupdate=func.now())

    conversation = relationship('Conversation')
    user = relationship('User')
    last_read_message = relationship('Message')

    def __init__(self, conversation_id: str, user_id: str, last_read_message_id: str):
        self.conversation_id = conversation_id
        self.user_id = user_id
        self.last_read_message_id = last_read_message_id
