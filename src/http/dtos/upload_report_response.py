from pydantic import BaseModel


class UploadReportResponse(BaseModel):
    message: str
