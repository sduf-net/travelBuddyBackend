from pydantic import BaseModel
from typing import Any, Optional

class SdufRequest(BaseModel):
    payload: Any
    user_id: str
    action: str
    user_token: Optional[str] = None
    screen_id: int
    project_id: str