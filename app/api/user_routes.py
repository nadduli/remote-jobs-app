#!/usr/bin/python3
"""
FastAPI router for user-related operations.
"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.session import get_db
