# Context: Mobile App 400 Errors

## Discussion
- The user reported 400 errors in the mobile app.
- Logs showed query parameters formatted like `hourly[]`.
- Analysis confirmed FastAPI doesn't automatically map these to list fields.
- User preferred to test the fix directly with the mobile app instead of running automated reproduction tests during the chat session.

## Notes
- The fix involves using `alias="field[]"` in Pydantic models and merging them in `to_params`.
- This pattern was applied to both Weather and Climate requests to ensure consistency.
