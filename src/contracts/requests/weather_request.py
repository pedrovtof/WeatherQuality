# pyrefly: ignore [missing-import]
from pydantic import BaseModel, Field
from typing import List, Optional, Union
# pyrefly: ignore [missing-import]
from fastapi import Query

class WeatherRequest(BaseModel):
    """
    Contract for Weather API requests based on Open-Meteo Air Quality API
    """
    latitude: float = Field(..., description="WGS84 coordinate")
    longitude: float = Field(..., description="WGS84 coordinate")
    hourly: Optional[List[str]] = Query(
        None, 
        description="List of hourly variables to retrieve"
    )
    domains: Optional[str] = Field("auto", description="auto, cams_europe, or cams_global")
    timeformat: Optional[str] = Field("iso8601", description="iso8601 or unixtime")
    timezone: Optional[str] = Field("GMT", description="Timezone name or auto")
    past_days: Optional[int] = Field(0, ge=0, le=92, description="Number of past days")
    forecast_days: Optional[int] = Field(5, ge=0, le=7, description="Number of forecast days")
    current: Optional[List[str]] = Query(None, description="Current variables")
    forecast_hours: Optional[int] = Field(None, description="Number of forecast hours")
    past_hours: Optional[int] = Field(None, description="Number of past hours")
    start_hour: Optional[str] = Field(None, description="YYYY-MM-DDTHH:MM")
    end_hour: Optional[str] = Field(None, description="YYYY-MM-DDTHH:MM")
    cell_selection: Optional[str] = Field("nearest", description="nearest, land, or sea")
    apikey: Optional[str] = Field(None, description="Commercial API key")
    start_date: Optional[str] = Field(None, pattern=r"^\d{4}-\d{2}-\d{2}$", description="YYYY-MM-DD")
    end_date: Optional[str] = Field(None, pattern=r"^\d{4}-\d{2}-\d{2}$", description="YYYY-MM-DD")

    def to_params(self) -> dict:
        """
        Convert to dictionary compatible with Open-Meteo API params
        """
        return self.model_dump(exclude_none=True)
