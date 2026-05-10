# Design: Model Selection UI

## Proposed UI Changes
- Add a "Climate Model" section above the Climate Trends chart.
- Use a horizontal `ScrollView` with selectable `Chips`.
- Default to `CMCC_CM2_VHR4` as it's the current one used in tests.

## State Management
- Add `availableModels` to `AppController` state.
- Add `selectedModel` to `AppController` state.
- Update `fetchData` to use `selectedModel`.

## Implementation Steps
1. Update `ApiInterfaces.ts` to include model types.
2. Update `ClimateService.ts` to include a method for fetching models.
3. Update `AppController.ts` to fetch models and manage selection state.
4. Update `Dashboard.tsx` to display the selection UI.
