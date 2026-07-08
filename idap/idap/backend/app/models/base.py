"""
Shared model mixin. Every table added from Take 2 onward (organizations,
users, datasets, KPIs, etc. — per Volume 2 Chapter 3) should inherit from
BaseModel so id/timestamp conventions stay consistent platform-wide.
"""
import uuid
from datetime import datetime, timezone

from sqlalchemy import Column, DateTime
from sqlalchemy.dialects.postgresql import UUID

from app.db.session import Base


class BaseModel(Base):
    __abstract__ = True

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    created_at = Column(DateTime(timezone=True), default=lambda: datetime.now(timezone.utc))
    updated_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )
