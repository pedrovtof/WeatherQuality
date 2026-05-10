# pyrefly: ignore [missing-import]
from fastapi import APIRouter

from src.services.healthcheck import healthcheck_message

router = APIRouter()

@router.get("/healthcheck")
def read_root():
    return healthcheck_message()
