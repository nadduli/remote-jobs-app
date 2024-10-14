#!/usr/bin/python3
"""
Database session management using SQLAlchemy.
Provides functions to interact with the PostgreSQL database asynchronously.
"""

from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings


engine = create_async_engine(settings.DATABASE_URL, echo=True)

local_session = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
    class_=AsyncSession
)

async def get_db():
     """
    Dependency to retrieve the current database session.
    Ensures that sessions are properly closed after use.
    """
     db = local_session()
     try:
          yield db
     finally:
          await db.close()