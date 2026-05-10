# Design: Mobile Application for Weather & Air Quality

## Architecture: MVC Pattern

### Models (`src/models/`)
- **WeatherModel**: Manages air quality data state.
- **ClimateModel**: Manages climate data state.
- **LocationModel**: Manages user coordinates and permissions.

### Views (`src/views/`)
- **DashboardScreen**: Main view showing current stats and quick filters.
- **WeatherDetailScreen**: Detailed charts for air quality.
- **ClimateDetailScreen**: Detailed charts for climate trends.
- **SettingsScreen**: (Optional) For preferences like units.

### Controllers (`src/controllers/`)
- **WeatherController**: Logic for fetching and filtering air quality data.
- **ClimateController**: Logic for fetching and filtering climate data.
- **LocationController**: Handles `expo-location` logic and updates models.

### Services (`src/services/`)
- **ApiClient**: Axios instance configured with base URL.
- **WeatherService**: Specific methods for `/weather`.
- **ClimateService**: Specific methods for `/climate`.

## UI/UX Design
- **Color Palette**: 
    - Air Quality: Greens (Good), Yellows (Moderate), Reds (Poor).
    - Climate: Blues (Cold), Oranges/Reds (Warm).
- **Responsive Layout**: Use Flexbox and percentage-based sizing.
- **Interaction**: Pull-to-refresh for data updates.

## Component Hierarchy
- `App.tsx` (Root)
    - `MainNavigator`
        - `TabNavigator`
            - `AirQualityTab` (Dashboard + Charts)
            - `ClimateTab` (Climate Charts + Filters)
        - `Modals/Loaders`

## Mock Testing Strategy
- Use `jest` to test Controllers and Services.
- Mock `expo-location` and `axios`.
- Snapshot testing for UI components.
