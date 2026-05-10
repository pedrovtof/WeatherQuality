from fastapi import APIRouter, Query
from typing import Annotated

from src.services.climate import Climate
from src.contracts.requests.climate_request import ClimateRequest

router = APIRouter()

@router.get("/climate")
def read_root(params: Annotated[ClimateRequest, Query()]):
    service = Climate()
    return service.get_daily_climate_values(params)

@router.get("/climate/models")
def get_models():
    service = Climate()
    return service.get_available_models()
