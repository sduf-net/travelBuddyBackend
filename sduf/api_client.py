from config import settings
import requests

BASE_URL = settings.SDUF_BASE_URL
PROJECT_TOKEN = settings.SDUF_PROJECT_TOKEN

def send_event(body):
    headers = {
        "Content-Type": "application/json",
        "x-project-token": PROJECT_TOKEN
    }
    response = requests.post(f"{BASE_URL}/api/v1/push/event", json=body, headers=headers)
    response.raise_for_status()
    return response
