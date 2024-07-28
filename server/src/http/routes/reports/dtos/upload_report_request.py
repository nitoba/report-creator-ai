from typing import Optional

from pydantic import BaseModel


class UploadReportRequest(BaseModel):
    user_id: str
    content: str
    title: Optional[str] = None
