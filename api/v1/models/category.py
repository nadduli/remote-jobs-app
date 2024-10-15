#!/usr/bin/python3
"""Category module"""

from sqlalchemy import Column, String
from app.db.base_model import Base


class Category(Base):
    """Class category which inherits from base_model"""

    __tablename__ = "categories"

    name = Column(String(50))
