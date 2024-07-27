from datetime import datetime

from pydantic import BaseModel


class UserPublic(BaseModel):
    id: str
    username: str
    email: str
    created_at: datetime
    updated_at: datetime
