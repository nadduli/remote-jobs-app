#!/usr/bin/python3
"""
Base class for SQLAlchemy models. All models will inherit from this base.
This base includes UUID as the primary key and auto-generated timestamps.
"""
import uuid
from sqlalchemy import Column, DateTime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import as_declarative, declared_attr
from sqlalchemy.sql import func


@as_declarative()
class Base:
    """
    Custom Base class for all SQLAlchemy models.
    Automatically generates a table name, uses UUID as the primary key,
    and includes 'created_at' and 'updated_at' timestamps.
    """

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, index=True)
    created_at = Column(
        DateTime(timezone=True), server_default=func.now(), nullable=False
    )
    updated_at = Column(DateTime(timezone=True), onupdate=func.now(), nullable=True)

    @declared_attr
    def __tablename__(cls) -> str:
        """
        Automatically derive table name from the class name.
        """
        return cls.__name__.lower()
