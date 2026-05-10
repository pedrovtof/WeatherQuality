"""
    Main router endpoints
"""

# pyrefly: ignore [missing-import]
from fastapi import APIRouter
from src.controllers import (
    healthcheck , weather
)

api_router = APIRouter()
api_router.include_router(healthcheck.router, tags=["health"])
api_router.include_router(weather.router, tags=["weather"])