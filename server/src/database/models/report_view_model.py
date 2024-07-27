import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship

from src.database.models.base import Base


class ReportViewModel(Base):
    __tablename__ = 'report_views'

    id = Column(String, primary_key=True, default=str(uuid.uuid4()))
    report_id = Column(String, ForeignKey('reports.id'), nullable=False)
    viewed_at = Column(DateTime, default=datetime.now)

    report = relationship('ReportModel', back_populates='views')
