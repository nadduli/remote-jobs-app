#!/usr/bin/python3
"""Handles crud operations for user module"""


from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.user import User
from app.models.enums import UserRole
from app.schemas.user import CreateUser
from app.utils.utils import hash_password


async def create_user(db: AsyncSession, create_user: CreateUser, role: UserRole):
    """Create a new user."""
    hashed_password = hash_password(create_user.password)

    user = User(
        username=create_user.username,
        email=create_user.email,
        password=hashed_password,
        role=role,
    )
    db.add(user)
    await db.commit()
    await db.refresh(user)
    return user


async def get_user(db: AsyncSession, user_id: str):
    """Retrieves a user by ID"""
    result = await db.execute(select(User).where(User.id == user_id))
    return result.scalars().first()


async def get_user_by_email(db: AsyncSession, email: str):
    result = await db.execute(select(User).where(User.email == email))
    return result.scalars().first()


async def update_user(
    db: AsyncSession, user_id: str, username: str, email: str, role: UserRole
):
    """Update user information."""
    user = await get_user(db, user_id)
    if user:
        user.username = username
        user.email = email
        user.role = role
        await db.commit()
        await db.refresh(user)
    return user


async def delete_user(db: AsyncSession, user_id: str):
    """Delete a user."""
    user = await get_user(db, user_id)
    if user:
        await db.delete(user)
        await db.commit()
    return user
