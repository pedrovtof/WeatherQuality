# Discovery: Date Range Selection

## Requirements
- Select start and end date for climate data.
- Limit: 90 days total (from current date or between start/end? User said "90 days forward or backward"). 
- Standard Open-Meteo Climate API limits usually apply, but the user wants a 90-day window.
- UI needs to be intuitive.

## Technical Details
- `ClimateParams` already has `start_date` and `end_date` as strings.
- Need a date picker or simple text inputs/buttons in the UI.
- Validation: Ensure `end_date` - `start_date` <= 90 days if that's the constraint, or simply that they are within 90 days of today. Re-reading: "limit to 90 days forward or back". This usually means the range itself can be anywhere, but the distance from "now" is limited, OR the duration is limited. Given Climate API constraints, I'll implement a duration limit and a "proximity to today" check if applicable.

## UI Components
- `RNDateTimePicker` is standard but requires a new dependency.
- For now, I'll use a simpler approach with basic buttons to increment/decrement weeks or a simple date string input if I want to avoid new native dependencies in this turn, OR I'll check if `expo` has a built-in one. `expo-date-picker` doesn't exist, it's usually `@react-native-community/datetimepicker`.
- I will use a simple "Period" selector with predefined ranges and custom inputs.
