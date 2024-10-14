from sqlalchemy import Column, String
from app.db.base_model import Base


class Company(Base):
    """Class to create categories"""

    __tablename__ = "companies"

    name = Column(String(50), index=True)
    description = Column(String(500))
    location = Column(String(100))
    website = Column(String(200))
