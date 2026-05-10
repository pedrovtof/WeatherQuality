# Discovery: 400 Bad Request on /weather

## Symptom
Log shows:
`"GET /weather?latitude=-23.546885760055996&longitude=-46.200914676404246&hourly%5B%5D=pm2_5&hourly%5B%5D=pm10&hourly%5B%5D=nitrogen_dioxide HTTP/1.1" 400 Bad Request`

## Analysis
- The client is sending `hourly[]` instead of `hourly`.
- `hourly[]` is a common convention in some libraries (like Axios or PHP) for sending arrays.
- FastAPI/Pydantic expects multiple `hourly` keys: `hourly=v1&hourly=v2`.
- When `hourly[]` is sent, Pydantic doesn't map it to the `hourly` field in `WeatherRequest`.
- Since `hourly` is optional, it might not be the cause of 400 UNLESS some other field is failing or there's strict validation.
- Wait, if `hourly[]` is sent and not defined, and if FastAPI is configured to reject extra params (not default), it could fail.
- But more likely, `hourly` is required by the underlying service but the contract says `Optional`.

Let's check `src/services/weather.py`.
