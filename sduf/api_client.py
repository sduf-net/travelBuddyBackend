from config import settings
import requests

BASE_URL = settings.SDUF_BASE_URL

def send_event(body):
    response = requests.post(f"{BASE_URL}/push/event", body)
    response.raise_for_status()
    return response.json()
