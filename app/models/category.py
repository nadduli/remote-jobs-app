from sqlalchemy import Column, String
from app.db.base_model import Base

class Category(Base):
    """Class to create categories"""

    __tablename__ = 'categories'
    
    name = Column(String(50))