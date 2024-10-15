#!/usr/bin/python3
"""user model"""

from pydantic import BaseModel, EmailStr
from uuid import UUID


class CreateUser(BaseModel):
    """model for creating a new user"""

    username: str
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    """model for returning user data"""

    id: UUID
    username: str
    email: EmailStr

    class Config:
        from_attributes = True
