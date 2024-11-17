import uuid
import json
from typing import Dict, Any

class ChatMessage():
    def __init__(self, data: Dict[str, Any]):
        self.id = uuid.uuid4(),
        self.name = "ChatMessageWidget",
        self.data = data

    def to_json(self) -> str:
        """
        Convert the instance to a JSON string.
        """
        return json.dumps(self, default=lambda obj: obj.__dict__, indent=4)