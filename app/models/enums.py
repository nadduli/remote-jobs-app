#!/usr/bin/python3

"""Enum class for User model"""

import enum


class UserRole(enum.Enum):
    admin = "admin"
    employers = "employers"
    job_seekers = "job_seekers"


class JobType(enum.Enum):
    full_time = "full_time"
    part_time = "part_time"
