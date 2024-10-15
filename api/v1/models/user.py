#!/usr/bin/python3
"""User Model"""

from sqlalchemy import Column, String, Enum
from .base_model import Base
from .enums import UserRole


class User(Base):
    """
    User model that inherits from Base.
    """

    username = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String)
    role = Column(Enum(UserRole), nullable=False)
