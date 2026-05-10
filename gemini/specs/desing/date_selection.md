# Design: Date Range Selection

## State
- `startDate`: string (YYYY-MM-DD)
- `endDate`: string (YYYY-MM-DD)

## UI
- A "Period" section in `Dashboard.tsx`.
- Two date displays that, when pressed, show a simple date adjustment interface (or just basic +/- buttons for simplicity and robustness without adding native deps now).
- I'll implement a helper to format and validate the dates.

## Validation Logic
- Max 90 days range.
- Dates should be within a reasonable window of today (Open-Meteo Climate API handles long ranges, but I'll stick to the "90 days" hint).
