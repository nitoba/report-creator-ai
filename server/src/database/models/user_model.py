import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, String
from sqlalchemy.orm import relationship

from src.database.models.base import Base


class UserModel(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True, default=str(uuid.uuid4()))
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(String)

    reports = relationship('ReportModel', back_populates='user')

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
