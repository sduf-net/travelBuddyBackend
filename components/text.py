import uuid
from components.base_component import BaseComponent


class Text(BaseComponent):
    def __init__(self, text: str, actions: dict = {}):
        self.id = str(uuid.uuid4()),
        self.name = "TextWidget",
        self.data = {
            "actions": actions,
            "text": text,
            "actions": actions
        }
