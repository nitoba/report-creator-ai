import uuid
from datetime import datetime
from typing import List

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, registry, relationship

from src.http.common.dtos.user_public import UserPublic

table_registry = registry()


@table_registry.mapped_as_dataclass
class UserModel:
    __tablename__ = 'users'

    id = Column(String, primary_key=True, default=str(uuid.uuid4()))
    username: Mapped[str] = Column(String, unique=True)
    email: Mapped[str] = Column(String, unique=True)
    password: Mapped[str] = Column(String)

    reports: Mapped[List['ReportModel']] = relationship(
        'ReportModel',
        back_populates='user',
        init=False,
        lazy='noload',
    )

    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def to_public(self):
        return UserPublic(
            id=self.id,
            username=self.username,
            email=self.email,
            created_at=self.created_at,
            updated_at=self.updated_at,
        )


@table_registry.mapped_as_dataclass
class ReportModel:
    __tablename__ = 'reports'

    id: Mapped[str] = Column(String, primary_key=True)
    user_id: Mapped[str] = Column(String, ForeignKey('users.id'), nullable=False)
    title: Mapped[str] = Column(String(255), nullable=False)
    file_id: Mapped[str] = Column(String(255), nullable=False)
    storage_url: Mapped[str] = Column(String(255), nullable=False)
    word_count: Mapped[int] = Column(Integer, nullable=False)
    created_at: Mapped[datetime] = Column(DateTime)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    user: Mapped['UserModel'] = relationship(
        'UserModel', back_populates='reports', init=False, lazy='noload'
    )
    views: Mapped[List['ReportViewModel']] = relationship(
        'ReportViewModel', back_populates='report', init=False, lazy='noload'
    )


@table_registry.mapped_as_dataclass
class ReportViewModel:
    __tablename__ = 'report_views'

    id = Column(String, primary_key=True, default=str(uuid.uuid4()))
    report_id = Column(String, ForeignKey('reports.id'), nullable=False)
    viewed_at = Column(DateTime, default=datetime.now)

    report: Mapped['ReportModel'] = relationship(
        'ReportModel', back_populates='views', init=False
    )
