# Discovery: Model Selection Feature

## Current State
- `Dashboard.tsx` triggers `fetchData` on mount.
- `AppController.ts` handles the fetching logic.
- Climate models are currently hardcoded or default to a single value in the request.

## Available Models
- The API has an endpoint `/climate/models` that returns available models.
- According to `test_weather.py`, there are 7 models, starting with `CMCC_CM2_VHR4`.

## UI Requirements
- A way to select one or more models (the API supports a list).
- Selection should happen before the climate request is executed.
- Maybe a horizontal scroll of chips or a modal/dropdown.

## Technical Considerations
- Need to fetch available models on app start.
- Store the selected model(s) in the controller state.
- Pass selected model(s) to `ClimateService.getClimateData`.
