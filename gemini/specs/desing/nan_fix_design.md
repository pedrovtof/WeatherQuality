# Design: NaN Serialization Fix

## Objective
Ensure that all API responses are JSON-compliant by replacing `NaN` values with `None`.

## Implementation Strategy
1. Add a static method `_sanitize_nan` to the `Openmeteo` class in `src/models/openmeteo_model.py`.
2. This method will recursively traverse dictionaries and lists.
3. Call this method at the end of `execute_api_air_request` and `execute_api_climate_request`.

## Modified Class Structure

```python
class Openmeteo:
    # ... existing methods ...

    @staticmethod
    def _sanitize_nan(obj):
        """
        Recursively replace NaN with None.
        """
        if isinstance(obj, float) and math.isnan(obj):
            return None
        elif isinstance(obj, list):
            return [Openmeteo._sanitize_nan(item) for item in obj]
        elif isinstance(obj, dict):
            return {k: Openmeteo._sanitize_nan(v) for k, v in obj.items()}
        return obj

    def execute_api_air_request(self, value : any) -> object:
        # ... existing logic ...
        return self._sanitize_nan(obj)

    def execute_api_climate_request(self, value : any) -> list:
        # ... existing logic ...
        return [self._sanitize_nan(res) for res in results]
```

## Verification Plan
1. Create a unit test in `src/tests/test_nan_fix.py` that mocks the API response with `NaN` values and verifies that `Openmeteo` returns `None` instead.
2. Run existing tests to ensure no regressions.
