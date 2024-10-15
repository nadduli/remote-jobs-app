#!/usr/bin/python3
"""job model"""

from sqlalchemy import Column, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from .base_model import Base
from api.v1.models.enums import JobType


class Job(Base):
    """Class Job which inherits from base_model"""

    __tablename__ = "jobs"

    title = Column(String, index=True)
    description = Column(String)
    location = Column(String)
    job_type = Column(Enum(JobType), nullable=False)
    salary_range = Column(String)
