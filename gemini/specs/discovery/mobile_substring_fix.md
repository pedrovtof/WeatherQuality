# Discovery: TypeError substring of undefined in Mobile App

## Symptom
Mobile app log shows:
`ERROR [TypeError: Cannot read property 'substring' of undefined]`

## Analysis
- Error occurs in `Dashboard.tsx` during label processing: `weatherData.time.map(t => t.split('T')[1].substring(0, 5))`.
- The API was returning time strings like `'2026-05-10 00:00:00+00:00'` (space separator).
- `t.split('T')[1]` was `undefined` because there was no 'T'.
- Calling `substring` on `undefined` caused the crash.

## Root Cause
- Backend used `pandas.astype(str)` which defaults to a space separator for datetimes.
- Frontend was not robust to different ISO8601 variations (space vs 'T').

## Solution
1. **Backend:** Force ISO8601 with 'T' separator using `.isoformat()`.
2. **Frontend:** Make the split logic robust to both space and 'T'.
