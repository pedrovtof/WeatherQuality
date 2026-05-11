import numpy as np
from unittest.mock import patch, MagicMock
from src.models.openmeteo_model import Openmeteo

def test_openmeteo_nan_sanitization():
    with patch("openmeteo_requests.Client") as mock_client_class:
        mock_client = mock_client_class.return_value
        
        # Setup mock response with NaN values
        mock_response = MagicMock()
        mock_response.Latitude.return_value = 52.52
        mock_response.Longitude.return_value = 13.41
        mock_response.Elevation.return_value = 10.0
        mock_response.UtcOffsetSeconds.return_value = 0
        mock_response.Timezone.return_value = b"UTC"
        mock_response.TimezoneAbbreviation.return_value = b"UTC"
        mock_response.GenerationTimeMilliseconds.return_value = 1.0
        
        # Current with NaN
        mock_current = MagicMock()
        mock_current.Time.return_value = 1715342400
        mock_var_current = MagicMock()
        mock_var_current.Value.return_value = float('nan')
        mock_current.Variables.return_value = mock_var_current
        mock_response.Current.return_value = mock_current
        
        # Hourly with NaN
        mock_hourly = MagicMock()
        mock_hourly.Time.return_value = 1715342400
        mock_hourly.TimeEnd.return_value = 1715346000
        mock_hourly.Interval.return_value = 3600
        
        mock_var_hourly = MagicMock()
        mock_var_hourly.ValuesAsNumpy.return_value = np.array([10.5, np.nan], dtype=np.float32)
        mock_hourly.Variables.return_value = mock_var_hourly
        
        mock_response.Hourly.return_value = mock_hourly
        mock_client.weather_api.return_value = [mock_response]
        
        model = Openmeteo()
        model._Openmeteo = mock_client
        model._Url = "http://mock-url"
        
        result = model.execute_api_air_request({
            "latitude": 52.52,
            "longitude": 13.41,
            "current": ["temperature_2m"],
            "hourly": ["pm10"]
        })
        
        # Verify NaN is replaced by None
        assert result["Current"]["temperature_2m"] is None
        assert result["Hourly"]["pm10"] == [10.5, None]

def test_sanitize_nan_logic():
    data = {
        "a": float('nan'),
        "b": [1.0, float('nan'), 2.0],
        "c": {"d": float('nan'), "e": "ok"}
    }
    sanitized = Openmeteo._sanitize_nan(data)
    assert sanitized["a"] is None
    assert sanitized["b"] == [1.0, None, 2.0]
    assert sanitized["c"]["d"] is None
    assert sanitized["c"]["e"] == "ok"
