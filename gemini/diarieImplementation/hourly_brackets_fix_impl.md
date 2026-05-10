# Implementation Diary - 2026-05-10

## Task: Fix 400 Bad Request for Mobile App

### 14:15 - Identification
- Analyzed logs and found `hourly[]` parameters.
- Hypothesis: FastAPI/Pydantic doesn't map `hourly[]` to `hourly` automatically.
- Reproduced the issue with a test case `src/tests/test_reproduce_400.py`, confirming `hourly` was missing in the internal params.

### 14:25 - Implementation
- Modified `src/contracts/requests/weather_request.py` to add `hourly_brackets` and `current_brackets` aliases.
- Modified `src/contracts/requests/climate_request.py` to add `models_brackets`, `current_brackets`, and `daily_brackets` aliases.
- Updated `to_params()` in both files to merge these bracketed fields into the standard ones.

### 14:35 - Verification (Pending)
- Ready to run `src/tests/test_reproduce_400.py` to confirm the fix.
- Will also run general tests.
