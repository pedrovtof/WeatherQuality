# Environment Variable Loading Design

## Objective
Enable `Openmeteo` model to load configuration from `src/.env`.

## Implementation
- Use `python-dotenv` to load the environment file.
- Since the model is in `src/models/`, the relative path to `.env` is `../.env`.
- Fix `os.environ("VAR")` (which is a syntax error, should be `os.environ.get("VAR")` or `os.getenv("VAR")`).
- Fix typo: `self._openmeteo` -> `self._Openmeteo`.

## Diary Update
### 2026-05-10 12:45
- Modified `src/models/openmeteo_model.py`.
- Added `load_dotenv` call pointing to `src/.env`.
- Corrected attribute access and environment fetching logic.
