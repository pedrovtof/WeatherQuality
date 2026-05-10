"""
    Main router endpoints
"""

# pyrefly: ignore [missing-import]
from fastapi import APIRouter
from src.controllers import (
    healthcheck, weather, climate
)

api_router = APIRouter()
api_router.include_router(healthcheck.router, tags=["health"])
api_router.include_router(weather.router, tags=["weather"])
api_router.include_router(climate.router, tags=["climate"])