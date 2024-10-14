#!/usr/bin/python3
"""user model"""

from pydantic import BaseModel
from uuid import UUID


class CreateUser(BaseModel):
    """model for creating a new user"""

    username: str
    email: str
    password: str


class UserResponse(BaseModel):
    """model for returning user data"""

    id: UUID
    username: str
    email: str

    class Config:
        orm_mode = True
