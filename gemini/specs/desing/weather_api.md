# Weather (Air Quality) API Documentation

This endpoint provides detailed air quality data using the Open-Meteo Air Quality API.

## Endpoint
`GET /weather`

## Request Parameters

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `latitude` | `float` | Yes | WGS84 coordinate. |
| `longitude` | `float` | Yes | WGS84 coordinate. |
| `hourly` | `List[str]` | No | List of variables: `pm10`, `pm2_5`, `carbon_monoxide`, `nitrogen_dioxide`, `sulphur_dioxide`, `ozone`, etc. |
| `domains` | `str` | No | `auto` (default), `cams_europe`, or `cams_global`. |
| `timezone` | `str` | No | Timezone name (e.g., `America/Sao_Paulo`) or `GMT` (default). |
| `past_days` | `int` | No | 0 to 92 days. |
| `forecast_days` | `int` | No | 0 to 7 days. |

## Usage Examples

### Basic Request
`GET /weather?latitude=-23.55&longitude=-46.63&hourly=pm10&hourly=pm2_5`

### Advanced Request
`GET /weather?latitude=-23.55&longitude=-46.63&hourly=pm10&hourly=ozone&timezone=America/Sao_Paulo&past_days=2`

## Response Structure

```json
{
  "message": "Sucess",
  "data": {
    "Latitude": -23.55,
    "Longitude": -46.63,
    "Elevation": 760.0,
    "UtcOffsetSeconds": -10800,
    "Timezone": "America/Sao_Paulo",
    "TimezoneAbbreviation": "-03",
    "Hourly": {
      "time": ["2026-05-10T00:00:00Z", ...],
      "pm10": [15.2, 14.8, ...],
      "ozone": [25.1, 24.5, ...]
    }
  }
}
```
