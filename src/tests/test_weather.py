from fastapi.testclient import TestClient
from src.app.main import app
from unittest.mock import patch, MagicMock

client = TestClient(app)

def test_weather_endpoint_params():
    # Mocking the service instead of the model for a broader test
    with patch("src.services.weather.Openmeteo") as mock_openmeteo_class:
        mock_instance = mock_openmeteo_class.return_value
        mock_instance.execute_api_air_request.return_value = {"mocked": "data"}
        
        # Test with multiple hourly params
        response = client.get("/weather?latitude=52.52&longitude=13.41&hourly=pm10&hourly=pm2_5")
        
        assert response.status_code == 200
        # Check if the mock was called with the correct parameters
        mock_instance.execute_api_air_request.assert_called_once()
        args, _ = mock_instance.execute_api_air_request.call_args
        params = args[0]
        
        assert params["latitude"] == 52.52
        assert params["longitude"] == 13.41
        assert "pm10" in params["hourly"]
        assert "pm2_5" in params["hourly"]
        
        # Check response structure
        data = response.json()
        assert data["message"] == "Sucess"
        assert data["data"] == {"mocked": "data"}

def test_weather_model_parsing():
    # Test the model logic directly
    from src.models.openmeteo_model import Openmeteo
    import numpy as np
    
    with patch("openmeteo_requests.Client") as mock_client_class:
        mock_client = mock_client_class.return_value
        
        # Setup mock response
        mock_response = MagicMock()
        mock_response.Latitude.return_value = 52.52
        mock_response.Longitude.return_value = 13.41
        mock_response.Elevation.return_value = 10.0
        mock_response.UtcOffsetSeconds.return_value = 0
        mock_response.Timezone.return_value = b"UTC"
        mock_response.TimezoneAbbreviation.return_value = b"UTC"
        
        mock_hourly = MagicMock()
        mock_hourly.Time.return_value = 1715342400 # Some timestamp
        mock_hourly.TimeEnd.return_value = 1715346000 # 1 hour later
        mock_hourly.Interval.return_value = 3600
        
        mock_var = MagicMock()
        mock_var.ValuesAsNumpy.return_value = np.array([10.5], dtype=np.float32)
        mock_hourly.Variables.return_value = mock_var
        
        mock_response.Hourly.return_value = mock_hourly
        mock_client.weather_api.return_value = [mock_response]
        
        model = Openmeteo()
        # Override the client to use our mock
        model._Openmeteo = mock_client
        model._Url = "http://mock-url"
        
        result = model.execute_api_air_request({
            "latitude": 52.52,
            "longitude": 13.41,
            "hourly": ["pm10"]
        })
        
        assert result["Latitude"] == 52.52
        assert "Hourly" in result
        assert "pm10" in result["Hourly"]
        assert result["Hourly"]["pm10"] == [10.5]
        assert "time" in result["Hourly"]

def test_climate_endpoint_params():
    with patch("src.services.climate.Openmeteo") as mock_openmeteo_class:
        mock_instance = mock_openmeteo_class.return_value
        mock_instance.execute_api_climate_request.return_value = [{"mocked": "climate_data"}]
        
        url = "/climate?latitude=41.40&longitude=2.17&start_date=2020-01-01&end_date=2020-01-02&models=CMCC_CM2_VHR4&daily=temperature_2m_max"
        response = client.get(url)
        
        assert response.status_code == 200
        mock_instance.execute_api_climate_request.assert_called_once()
        data = response.json()
        assert data["message"] == "Sucess"
        assert data["data"] == [{"mocked": "climate_data"}]

def test_weather_endpoint_error():
    with patch("src.services.weather.Openmeteo") as mock_openmeteo_class:
        mock_instance = mock_openmeteo_class.return_value
        mock_instance.execute_api_air_request.side_effect = Exception("API Error")
        
        response = client.get("/weather?latitude=52.52&longitude=13.41")
        
        assert response.status_code == 400
        
        data = response.json()
        assert data["message"] == "An error occurred during the request"

def test_climate_endpoint_error():
    with patch("src.services.climate.Openmeteo") as mock_openmeteo_class:
        mock_instance = mock_openmeteo_class.return_value
        mock_instance.execute_api_climate_request.side_effect = Exception("API Error")
        
        url = "/climate?latitude=41.40&longitude=2.17&start_date=2020-01-01&end_date=2020-01-02&models=CMCC_CM2_VHR4"
        response = client.get(url)
        
        assert response.status_code == 400
        
        data = response.json()
        assert data["message"] == "An error occurred during the request"

def test_get_climate_models():
    response = client.get("/climate/models")
    assert response.status_code == 200
    data = response.json()
    assert data["message"] == "Sucess"
    assert len(data["data"]) == 7
    assert data["data"][0]["model"] == "CMCC_CM2_VHR4"
