from config import settings
from sduf.api_client import send_event
from schemas.sduf_request.sduf_request import SdufEvent
import uuid

BASE_URL = settings.SDUF_BASE_URL

def test_sign_in_success(mock_requests_post):
    event = SdufEvent(
        event_id=str(uuid.uuid4()),
        user_id=str(uuid.uuid4()),
        project_id=str(uuid.uuid4()),
        screen_id=str(uuid.uuid4()),
        action="show_error_message",
        payload={}
    )
    send_event(event)
    mock_requests_post.assert_called_once()
