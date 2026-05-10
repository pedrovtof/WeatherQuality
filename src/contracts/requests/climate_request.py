# pyrefly: ignore [missing-import]
from pydantic import BaseModel, Field, model_validator
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
    models: Optional[List[str]] = Query(None, description="Climate models to use")
    models_brackets: Optional[List[str]] = Query(
        None, 
        alias="models[]", 
        include_in_schema=False
    )
    current: Optional[List[str]] = Query(None, description="Current variables")
    current_brackets: Optional[List[str]] = Query(
        None, 
        alias="current[]", 
        include_in_schema=False
    )
    daily: Optional[List[str]] = Query(None, description="List of daily variables to retrieve")
    daily_brackets: Optional[List[str]] = Query(
        None, 
        alias="daily[]", 
        include_in_schema=False
    )
    timezone: Optional[str] = Field("America/Sao_Paulo", description="Timezone name")

    @model_validator(mode='after')
    def check_models_present(self) -> 'ClimateRequest':
        if not self.models and not self.models_brackets:
            raise ValueError("At least one of 'models' or 'models[]' must be provided")
        return self

    def to_params(self) -> dict:
        """
        Convert to dictionary compatible with Open-Meteo API params
        """
        params = self.model_dump(exclude_none=True)

        # Merge bracketed versions if they exist
        if "models_brackets" in params:
            models = params.get("models", [])
            params["models"] = list(set(models + params.pop("models_brackets")))
        
        if "current_brackets" in params:
            current = params.get("current", [])
            params["current"] = list(set(current + params.pop("current_brackets")))
        
        if "daily_brackets" in params:
            daily = params.get("daily", [])
            params["daily"] = list(set(daily + params.pop("daily_brackets")))

        return params
