"""
    Main file startup
"""

# pyrefly: ignore [missing-import]
from fastapi import FastAPI
from src.router.router import api_router

app = FastAPI()

app.include_router(api_router)
