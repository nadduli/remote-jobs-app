#!/usr/bin/python3
"""
Database session management using SQLAlchemy.
Provides functions to interact with the PostgreSQL database asynchronously.
"""

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings

# Create the asynchronous engine
engine = create_async_engine(settings.DATABASE_URL, echo=True)

# Create a sessionmaker factory for AsyncSession
local_session = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autocommit=False,
    autoflush=False,
)


async def get_db():
    """
    Dependency to retrieve the current database session.
    Ensures that sessions are properly closed after use.
    """
    async with local_session() as db:
        yield db
