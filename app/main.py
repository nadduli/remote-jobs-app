#!/usr/bin/python3
"""
Main entry point of the FastAPI application.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.session import get_db, engine
from app.db.base_model import Base
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import text
from app.models.user import User
from app.api.user_routes import router as user_router


app = FastAPI()

# CORS Middleware setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    """
    Check database connection on startup and create tables if needed.
    """
    try:
        # Directly use AsyncSession here
        async with engine.begin() as conn:  # Ensure we use the engine
            result = await conn.execute(text("SELECT 1"))
            print("Database connection successful.")

            # Create tables
            await conn.run_sync(Base.metadata.create_all)

    except Exception as e:
        print(f"Database connection failed: {e}")


app.include_router(user_router, prefix="/api", tags=["users"])


@app.get("/")
async def root():
    """
    Simple root endpoint to ensure the app is running.
    """
    return {"message": "Welcome to the Remote Job Listing API"}
