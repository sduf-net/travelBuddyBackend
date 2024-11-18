import json

class BaseComponent():
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