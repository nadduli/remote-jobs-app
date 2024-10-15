# models/your_model.py
from sqlalchemy import Column, String, Enum
from app.db.base_model import Base
from app.models.enums import UserRole


class User(Base):
    """
    User model that inherits from Base.
    """

    username = Column(String(50), nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    password = Column(String)
    role = Column(Enum(UserRole), nullable=False)
