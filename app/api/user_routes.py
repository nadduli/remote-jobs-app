#!/usr/bin/python3
"""
FastAPI router for user-related operations.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
from app.models.user import User
from app.models.enums import UserRole
from app.db.user_crud import (
    create_user,
    get_user,
    update_user,
    delete_user,
    get_user_by_email,
)
from app.schemas.user import CreateUser, UserResponse


router = APIRouter()


@router.post("/users/", response_model=UserResponse)
async def create_new_user(
    create_user_data: CreateUser, role: UserRole, db: AsyncSession = Depends(get_db)
):
    """Create a new user."""
    userExists = await get_user_by_email(db, create_user_data.email)

    if userExists:
        raise HTTPException(status_code=400, detail="Email already registered")

    user = await create_user(db, create_user_data, role)
    return UserResponse.model_validate(user)


@router.get("/users/{user_id}", response_model=UserResponse)
async def read_user(user_id: str, db: AsyncSession = Depends(get_db)):
    """Retrieve a user by ID."""
    user = await get_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return UserResponse.model_validate(user)


@router.put("/users/{user_id}", response_model=UserResponse)
async def update_existing_user(
    user_id: str,
    user_update: CreateUser,
    role: UserRole,
    db: AsyncSession = Depends(get_db),
):
    """Update an existing user."""
    user = await update_user(db, user_id, user_update.username, user_update.email, role)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return UserResponse.model_validate(user)


@router.delete("/users/{user_id}", response_model=UserResponse)
async def remove_user(user_id: str, db: AsyncSession = Depends(get_db)):
    """Delete a user."""
    user = await delete_user(db, user_id)
    if user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return UserResponse.model_validate(user)
