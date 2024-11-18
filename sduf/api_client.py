from config import get_settings
import requests
from schemas.sduf_request.sduf_request import SdufEvent

BASE_URL = get_settings().SDUF_BASE_URL
PROJECT_TOKEN = get_settings().SDUF_PROJECT_TOKEN

def send_event(body: SdufEvent):
    headers = {
        "Content-Type": "application/json",
        "x-project-token": PROJECT_TOKEN
    }
    response = requests.post(f"{BASE_URL}/api/v1/push/event", json=body, headers=headers)
    response.raise_for_status()
    return response
