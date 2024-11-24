import uuid
from components.base_component import BaseComponent


class Image(BaseComponent):
    def __init__(self, image_url: str, alt: str | None = None, actions: dict = {}):
        self.id = str(uuid.uuid4()),
        self.name = "ImageWidget",
        self.data = {
            "actions": actions,
            "alt": alt,
            "src": image_url
        }
