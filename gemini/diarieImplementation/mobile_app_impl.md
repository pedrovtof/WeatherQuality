# Implementation Diary: Mobile Application

## Date: 2026-05-10

### Accomplishments
- Initialized Expo Go project with TypeScript in `mobile/`.
- Implemented MVC architecture:
    - **Model**: Defined types and interfaces in `src/interfaces/ApiInterfaces.ts`.
    - **Controller**: 
        - `LocationController` for permissions and GPS logic.
        - `AppController` (Custom Hook) for orchestrating data flow between services and views.
    - **View**:
        - `Dashboard` with summary stats and charts.
        - `ChartComponent` as a reusable wrapper for `react-native-chart-kit`.
- Integrated `expo-location` for automatic user positioning.
- Integrated `axios` for backend communication with repeated param support (for hourly/daily/models).
- Added `lucide-react-native` for modern UI icons.
- Configured Jest and wrote mocked tests for Services and Controllers.

### Technical Challenges
- **React 19 & Jest**: Encountered version mismatch between `jest-expo`, `react-test-renderer`, and `react`. Resolved by manually aligning versions in `package.json` and using `--legacy-peer-deps`.
- **Responsive Charts**: Implemented dynamic width calculations using `Dimensions` to ensure charts fit different screen sizes.

### UI/UX Decisions
- Used `SafeAreaView` and `ScrollView` for cross-platform compatibility.
- Implemented Pull-to-Refresh (`RefreshControl`) for easy data updates.
- Added visual feedback for loading and error states.

### Verification
- Ran `npm test` in the `mobile/` directory:
    - `WeatherService.test.ts`: PASS
    - `AppController.test.ts`: PASS
