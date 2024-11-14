from pydantic import BaseModel
from typing import Any, Optional

class SdufRequest(BaseModel):
    payload: Any
    user_id: str
    action: str
    user_token: Optional[str] = None
    screen_id: int
    project_id: str

class SdufEvent(BaseModel):
    payload: Any
    event_id: str
    user_id: str
    project_id: str
    screen_id: str
    action: str