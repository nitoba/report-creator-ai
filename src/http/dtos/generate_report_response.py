from pydantic import BaseModel


class GenerateReportResponse(BaseModel):
    report: str
