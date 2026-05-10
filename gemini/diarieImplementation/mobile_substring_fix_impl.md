# Implementation Diary - 2026-05-10

## Task: Fix 400 Bad Request for Mobile App (Completed)
- Supported `hourly[]` etc. in API contracts.
- Fixed `URL_API_OPEN_METEO` in `.env`.

## Task: Fix 'substring of undefined' in Mobile App

### 14:50 - Identification
- Found usage of `.split('T')[1].substring(0, 5)` in `Dashboard.tsx`.
- Confirmed API was sending space-separated timestamps.

### 15:00 - Implementation
- **Backend:** Updated `src/models/openmeteo_model.py` to use `.isoformat()` for all timestamps.
- **Frontend:** Updated `mobile/src/views/Dashboard.tsx` to split by `/[T ]/` (regex) to handle both formats.

### 15:10 - Verification
- Fixed `react-test-renderer` dependency in mobile project.
- Ran `npm test` in `mobile/` - all 3 tests passed.
- Integration test for API already confirmed the fix for 400, now it also verifies ISO format.

## Task: Fix 422 Unprocessable Content for Climate Endpoint

### 15:20 - Identification
- Found that `models` field was required in `ClimateRequest`.
- Client sends `models[]`, which Pydantic doesn't map to the required `models` field.

### 15:25 - Implementation
- Modified `src/contracts/requests/climate_request.py` to make `models` optional.
- Added `@model_validator` to ensure at least `models` or `models[]` is provided.

### 15:30 - Verification
- Reproduced with `src/tests/test_reproduce_422.py`.
- Verified fix returns `200 OK`.
