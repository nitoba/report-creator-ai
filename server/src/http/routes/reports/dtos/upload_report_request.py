from typing import Optional

from pydantic import BaseModel


class UploadReportRequest(BaseModel):
    content: str
    title: Optional[str]
