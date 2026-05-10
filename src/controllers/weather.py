# pyrefly: ignore [missing-import]
from fastapi import APIRouter

from src.services.weather import Weather

router = APIRouter()

@router.get("/weather")
def read_root():
    service = Weather()
    return service.get_hourly_air_quality_values()
