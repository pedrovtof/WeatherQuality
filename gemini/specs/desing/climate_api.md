# Climate API Documentation

This endpoint provides climate projections and historical data based on various climate models using the Open-Meteo Climate API.

## Endpoint
`GET /climate`

## Request Parameters

| Parameter | Type | Required | Description |
| :--- | :--- | :--- | :--- |
| `latitude` | `float` | Yes | WGS84 coordinate. |
| `longitude` | `float` | Yes | WGS84 coordinate. |
| `start_date` | `str` | Yes | Start date in `YYYY-MM-DD` format. |
| `end_date` | `str` | Yes | End date in `YYYY-MM-DD` format. |
| `models` | `List[str]` | Yes | List of climate models. Ver modelos disponíveis abaixo. |
| `daily` | `List[str]` | No | List of variables: `temperature_2m_max`, `temperature_2m_min`, `precipitation_sum`, etc. |
| `timezone` | `str` | No | Timezone name (default: `America/Sao_Paulo`). |

## Available Climate Models

A API utiliza modelos de alta resolução (10 km) do projeto IPCC CMIP6. Os modelos suportados são:

| Modelo (String) | Instituição / País |
| :--- | :--- |
| `CMCC_CM2_VHR4` | Euro-Mediterranean Center on Climate Change (Itália) |
| `FGOALS_f3_H` | Chinese Academy of Sciences (China) |
| `HiRAM_SIT_HR` | NOAA (EUA) |
| `MRI_AGCM3_2_S` | Meteorological Research Institute (Japão) |
| `EC_Earth3P_HR` | EC-Earth Consortium (Europa) |
| `MPI_ESM1_2_XR` | Max Planck Institute for Meteorology (Alemanha) |
| `NICAM16_8S` | University of Tokyo / RIKEN (Japão) |

> **Nota**: Dados de umidade do solo (`soil_moisture`) estão disponíveis apenas nos modelos `MRI_AGCM3_2_S` e `EC_Earth3P_HR`.

## Usage Examples

### Basic Request
`GET /climate?latitude=-23.56&longitude=-46.18&start_date=2026-01-01&end_date=2026-05-01&models=CMCC_CM2_VHR4&daily=temperature_2m_max`

### Multiple Models Request
`GET /climate?latitude=-23.56&longitude=-46.18&start_date=2026-01-01&end_date=2026-05-01&models=CMCC_CM2_VHR4&models=FGOALS_f3_H&daily=temperature_2m_max`

## Response Structure

The response returns a list of objects, one for each requested climate model.

```json
{
  "message": "Sucess",
  "data": [
    {
      "Latitude": -23.56,
      "Longitude": -46.18,
      "Elevation": 740.0,
      "UtcOffsetSeconds": -10800,
      "Timezone": "America/Sao_Paulo",
      "TimezoneAbbreviation": "-03",
      "Model": "CMCC_CM2_VHR4",
      "Daily": {
        "time": ["2026-01-01", ...],
        "temperature_2m_max": [28.5, 27.2, ...]
      }
    }
  ]
}
```
