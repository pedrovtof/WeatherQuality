# Bug Investigation: AttributeError in response_api.py

## Observations
- In `src/contracts/response_api.py`, the `__init__` method initializes variables like `_Status`, `_Message`, and `_Return` as local variables instead of instance attributes (missing `self.`).
- The `set_status` method attempts to access `self._Status` before it is ever assigned to the instance.
- In `src/contracts/response_sucess_api.py`, `_Details` is also initialized as a local variable.

## Root Cause
Incorrect use of instance attributes in `__init__` across contract classes. Variables are defined without `self.`.

## Strategy
1. Fix `src/contracts/response_api.py` to use `self._Status`, `self._Message`, etc.
2. Fix `src/contracts/response_sucess_api.py` to use `self._Details`.
3. Check `src/contracts/response_error_api.py` for similar issues.
