# Design: Safer set_details implementation

## Objective
Refactor `ResponseSucessApi.set_details` to safely handle any object type.

## Proposed Changes
1. Update `set_details` to use `is None` for null check.
2. Use `isinstance(value, dict)` before checking `len(value) == 0` to avoid ambiguous truth value errors on non-dict objects.
3. Fix tests in `src/tests/test_contracts.py` and `src/tests/test_main.py` to match the actual API contract (key "data", message "Alive").

## Verification Plan
- Create a reproduction script `reproduce_issue.py` with numpy arrays and custom objects.
- Run `pytest` on existing tests.
