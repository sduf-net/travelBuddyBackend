from config import get_settings
import requests
from schemas.sduf_request.sduf_request import SdufEvent

BASE_URL = get_settings().SDUF_BASE_URL
PROJECT_TOKEN_API = get_settings().SDUF_PROJECT_TOKEN

def send_event(body: SdufEvent):
    print(f"Send Event {body.action}")
    headers = {
        "Content-Type": "application/json",
        "x-api-token": PROJECT_TOKEN_API
    }
    response = requests.post(f"{BASE_URL}/api/v1/push/event", json=body.model_dump(), headers=headers)
    response.raise_for_status()
    return response
