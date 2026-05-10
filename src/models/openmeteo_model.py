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
        self._Climate_Url = os.getenv("URL_API_CLIMATE_OPEN_METEO", "https://climate-api.open-meteo.com/v1/climate")
        self._Param = None

        return

    def execute_api_air_request(self, value : any) -> object:
        """
            Execute a request to air quality api with param
        """

        self._Param = value

        meteo_responses = self._Openmeteo.weather_api(self._Url, params = self._Param)
        response = meteo_responses[0]

        obj = {
            "Latitude": response.Latitude(),
            "Longitude": response.Longitude(),
            "Elevation" : response.Elevation(),
            "UtcOffsetSeconds" : response.UtcOffsetSeconds(),
            "Timezone": response.Timezone().decode() if isinstance(response.Timezone(), bytes) else response.Timezone(),
            "TimezoneAbbreviation": response.TimezoneAbbreviation().decode() if isinstance(response.TimezoneAbbreviation(), bytes) else response.TimezoneAbbreviation(),
            "GenerationTimeMilliseconds": response.GenerationTimeMilliseconds()
        }

        # Extract current data
        current = response.Current()
        if current:
            current_data = {
                "time": pd.to_datetime(current.Time(), unit="s", utc=True).isoformat()
            }
            current_params = self._Param.get("current", [])
            if isinstance(current_params, str):
                current_params = [current_params]
            
            for i, var_name in enumerate(current_params):
                current_data[var_name] = current.Variables(i).Value()
            
            obj["Current"] = current_data

        # Extract hourly data
        hourly = response.Hourly()
        if hourly:
            hourly_data = {
                "time": [t.isoformat() for t in pd.date_range(
                    start=pd.to_datetime(hourly.Time(), unit="s", utc=True),
                    end=pd.to_datetime(hourly.TimeEnd(), unit="s", utc=True),
                    freq=pd.Timedelta(seconds=hourly.Interval()),
                    inclusive="left"
                )]
            }

            hourly_params = self._Param.get("hourly", [])
            if isinstance(hourly_params, str):
                hourly_params = [hourly_params]

            for i, var_name in enumerate(hourly_params):
                hourly_data[var_name] = hourly.Variables(i).ValuesAsNumpy().tolist()

            obj["Hourly"] = hourly_data

        return obj

    def execute_api_climate_request(self, value : any) -> list:
        """
            Execute a request to climate api with param
        """
        self._Param = value

        meteo_responses = self._Openmeteo.weather_api(self._Climate_Url, params = self._Param)

        results = []

        for response in meteo_responses:
            obj = {
                "Latitude": response.Latitude(),
                "Longitude": response.Longitude(),
                "Elevation" : response.Elevation(),
                "UtcOffsetSeconds" : response.UtcOffsetSeconds(),
                "Timezone": response.Timezone().decode() if isinstance(response.Timezone(), bytes) else response.Timezone(),
                "TimezoneAbbreviation": response.TimezoneAbbreviation().decode() if isinstance(response.TimezoneAbbreviation(), bytes) else response.TimezoneAbbreviation(),
                "GenerationTimeMilliseconds": response.GenerationTimeMilliseconds(),
                "Model": response.Model()
            }

            # Extract current data
            current = response.Current()
            if current:
                current_data = {
                    "time": pd.to_datetime(current.Time(), unit="s", utc=True).isoformat()
                }
                current_params = self._Param.get("current", [])
                if isinstance(current_params, str):
                    current_params = [current_params]
                
                for i, var_name in enumerate(current_params):
                    current_data[var_name] = current.Variables(i).Value()
                
                obj["Current"] = current_data

            daily = response.Daily()
            if daily:
                daily_data = {
                    "time": [t.isoformat() for t in pd.date_range(
                        start=pd.to_datetime(daily.Time(), unit="s", utc=True),
                        end=pd.to_datetime(daily.TimeEnd(), unit="s", utc=True),
                        freq=pd.Timedelta(seconds=daily.Interval()),
                        inclusive="left"
                    )]
                }

                daily_params = self._Param.get("daily", [])
                if isinstance(daily_params, str):
                    daily_params = [daily_params]

                for i, var_name in enumerate(daily_params):
                    daily_data[var_name] = daily.Variables(i).ValuesAsNumpy().tolist()

                obj["Daily"] = daily_data

            results.append(obj)

        return results

