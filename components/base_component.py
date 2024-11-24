import json
import uuid


class BaseComponent():
    def __init__(self):
        self.id = str(uuid.uuid4()),
        self.name = None,
        self.data = {}

    def to_json(self) -> str:
        """
        Convert the instance to a JSON string.
        """
        return json.dumps(self, default=lambda obj: obj.__dict__, indent=4)

    def to_dict(self) -> dict:
        """
        Converts the instance to a dictionary.
        """
        return {
            "id": self.id,
            "name": self.name,
            "data": self.data
        }
