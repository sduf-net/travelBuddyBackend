import uuid
from components.base_component import BaseComponent

class ChatMessage(BaseComponent):
    def __init__(self, name: str, text: str, date: str, is_owner: str = False, actions: dict = {}):
        self.id = str(uuid.uuid4()),
        self.name = "ChatMessageWidget",
        self.data = {
            "name": name,
            "text": text,
            "date": date,
            "is_owner": is_owner,
            "actions": actions
        }
