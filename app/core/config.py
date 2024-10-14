#!/usr/bin/python3
"""
Configuration file that loads environment variables and settings
"""

from pydantic_settings import BaseSettings



class Settings(BaseSettings):
    """load application settings from environment variables
     defined in the .env file
       """
    DATABASE_URL: str

    class Config:
        env_file = ".env"

settings = Settings()