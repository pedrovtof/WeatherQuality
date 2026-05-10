# pyrefly: ignore [missing-import]
import openmeteo_requests
import os
import pandas as pd
# pyrefly: ignore [missing-import]
import requests_cache
# pyrefly: ignore [missing-import]
from retry_requests import retry
# pyrefly: ignore [missing-import]
from dotenv import load_dotenv

class Openmeteo:
    def __init__(self):
        """
            Setup the Open-Meteo API client with cache and retry on error
        """
        load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

        self._Cache_session =  requests_cache.CachedSession('.cache', expire_after = 3600)
        self._Retry_session = retry(self._Cache_session, retries = 3, backoff_factor = 0.2)
        self._Openmeteo = openmeteo_requests.Client(session = self._Retry_session)
        self._Url = os.getenv("URL_API_OPEN_METEO")
        self._Param = None

        return

    def execute_api_request(self, value : any) -> object:
        """
            Execute a request to meteo with param
        """

        self._Param = value

        meteo_responses = self._Openmeteo.weather_api(self._Url, params = self._Param)

        obj = {
            "Latitude": meteo_responses[0].Latitude(),
            "Longitude": meteo_responses[0].Longitude(),
            "Elevation" : meteo_responses[0].Elevation(),
            "UtcOffsetSeconds" : meteo_responses[0].UtcOffsetSeconds()
        }

        return obj
