from fastapi import APIRouter, Query
from typing import Annotated

from src.services.weather import Weather
from src.contracts.requests.weather_request import WeatherRequest

router = APIRouter()

@router.get("/weather")
def read_root(params: Annotated[WeatherRequest, Query()]):
    service = Weather()
    return service.get_hourly_air_quality_values(params)
