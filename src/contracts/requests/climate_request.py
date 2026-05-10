# pyrefly: ignore [missing-import]
from pydantic import BaseModel, Field
from typing import List, Optional
# pyrefly: ignore [missing-import]
from fastapi import Query

class ClimateRequest(BaseModel):
    """
    Contract for Climate API requests based on Open-Meteo Climate API
    """
    latitude: float = Field(..., description="WGS84 coordinate")
    longitude: float = Field(..., description="WGS84 coordinate")
    start_date: str = Field(..., pattern=r"^\d{4}-\d{2}-\d{2}$", description="YYYY-MM-DD")
    end_date: str = Field(..., pattern=r"^\d{4}-\d{2}-\d{2}$", description="YYYY-MM-DD")
    models: List[str] = Query(..., description="Climate models to use")
    current: Optional[List[str]] = Query(None, description="Current variables")
    daily: Optional[List[str]] = Query(None, description="List of daily variables to retrieve")
    timezone: Optional[str] = Field("America/Sao_Paulo", description="Timezone name")

    def to_params(self) -> dict:
        """
        Convert to dictionary compatible with Open-Meteo API params
        """
        return self.model_dump(exclude_none=True)
