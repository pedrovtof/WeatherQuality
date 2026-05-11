# Discovery: NaN Serialization Error

## Problem
The FastAPI application fails with `ValueError: Out of range float values are not JSON compliant: nan` when the response data contains `NaN` values. This typically happens when the Open-Meteo API returns missing data for some variables.

## Traceback Analysis
The error occurs in `starlette/responses.py` during `json.dumps`. Starlette's `JSONResponse` seems to be configured (or defaulting in Python 3.13) to be strict about JSON compliance, rejecting `NaN`.

## Origin of NaN
- `src/models/openmeteo_model.py`:
  - `current.Variables(i).Value()` can return `NaN`.
  - `hourly.Variables(i).ValuesAsNumpy().tolist()` can contain `NaN`.
  - `daily.Variables(i).ValuesAsNumpy().tolist()` can contain `NaN`.

## Proposed Solution
Implement a recursive function to replace all `NaN` values with `None` in the response dictionary before it's sent to the controller.

```python
import math

def sanitize_nan(obj):
    if isinstance(obj, float) and math.isnan(obj):
        return None
    elif isinstance(obj, list):
        return [sanitize_nan(item) for item in obj]
    elif isinstance(obj, dict):
        return {k: sanitize_nan(v) for k, v in obj.items()}
    return obj
```

## Next Steps
1. Create a design spec for the fix.
2. Implement the `sanitize_nan` logic.
3. Apply it to the `Openmeteo` class methods.
4. Verify the fix.
