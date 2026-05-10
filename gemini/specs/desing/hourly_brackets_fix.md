# Design: Handling Bracketed Query Parameters

## Problem
Clients (e.g. mobile apps using certain libraries) send array parameters with `[]` suffix, like `hourly[]=pm2_5`. FastAPI/Pydantic expects just `hourly=pm2_5`.

## Solution
Modify `WeatherRequest` contract to accept both forms.

### Approach 1: Dual Fields
```python
    hourly: Optional[List[str]] = Query(None)
    hourly_brackets: Optional[List[str]] = Query(None, alias="hourly[]", include_in_schema=False)
```
Then in `to_params`:
```python
    def to_params(self) -> dict:
        params = self.model_dump(exclude_none=True)
        if "hourly_brackets" in params:
            params["hourly"] = params.get("hourly", []) + params.pop("hourly_brackets")
        return params
```

### Approach 2: AliasChoices (Pydantic v2)
FastAPI might not support `AliasChoices` for Query parameters directly in the same way it does for body.

### Decision
Use Approach 1 as it is more explicit and guaranteed to work with FastAPI's `Query` parameter extraction.

## Files to modify
- `src/contracts/requests/weather_request.py`
- `src/contracts/requests/climate_request.py` (if it has similar fields)

## Verification
- Run `src/tests/test_reproduce_400.py` and ensure `hourly` is present in params even when sent as `hourly[]`.
- Run all existing tests to ensure no regressions.
