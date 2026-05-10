# Router Design

## Objective
Establish a scalable routing structure for the FastAPI application.

## Structure
- `src/interfaces/api/router.py`: Main router aggregator.
- `src/interfaces/api/endpoints/`: Directory for specific route modules.
    - `health.py`: Healthcheck routes.
    - `weather.py`: (Future) Weather related routes.

## Implementation Steps
1. Create directories: `src/interfaces/api/endpoints`.
2. Create `src/interfaces/api/endpoints/health.py` with the `/healthcheck` route.
3. Create `src/interfaces/api/router.py` to include `health` router.
4. Modify `src/app/main.py` to include the main router.

## Testing
- Run the server and check `http://localhost:8000/healthcheck`.
- Check `/docs` for generated OpenAPI spec.
