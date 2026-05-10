# Router Setup Context

The user wants to create a router for the Python (FastAPI) application.
Currently, `main.py` contains all logic. I should move routes to a dedicated directory (e.g., `src/interfaces/api/routes`) or similar, depending on the project's architecture.

Architecture observed:
- src/app/main.py
- src/services/
- src/models/
- src/interfaces/
- src/infra/
- src/helpers/

This looks like a Clean Architecture or Hexagonal structure. Routes usually go into `interfaces`.
