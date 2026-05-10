# Discovery: Mobile Application for Weather & Air Quality

## Overview
The mobile app will be built using React Native with Expo Go. It will provide real-time air quality and climate data based on the user's current location, fetched from the existing FastAPI backend.

## Backend Endpoints Integration

### 1. Healthcheck
- **Endpoint**: `GET /healthcheck`
- **Purpose**: Verify backend availability.

### 2. Air Quality (Weather)
- **Endpoint**: `GET /weather`
- **Params**:
    - `latitude`: float
    - `longitude`: float
    - `hourly`: List of strings (e.g., `pm10`, `pm2_5`, `carbon_monoxide`, `nitrogen_dioxide`, `sulphur_dioxide`, `ozone`)
- **Response Structure**:
    ```json
    {
      "message": "Sucess",
      "data": {
        "Hourly": {
          "time": [...],
          "pm10": [...],
          ...
        }
      }
    }
    ```

### 3. Climate Data
- **Endpoint**: `GET /climate`
- **Params**:
    - `latitude`: float
    - `longitude`: float
    - `start_date`: YYYY-MM-DD
    - `end_date`: YYYY-MM-DD
    - `models`: List of strings
    - `daily`: List of strings (e.g., `temperature_2m_max`, `temperature_2m_min`)
- **Response Structure**:
    ```json
    {
      "message": "Sucess",
      "data": [
        {
          "Model": "...",
          "Daily": {
            "time": [...],
            "temperature_2m_max": [...],
            ...
          }
        }
      ]
    }
    ```

### 4. Climate Models
- **Endpoint**: `GET /climate/models`
- **Purpose**: Fetch available climate models for filtering.

## Mobile Requirements

### Tech Stack
- **Framework**: Expo Go (React Native)
- **Pattern**: MVC (Model-View-Controller)
- **Location**: `expo-location`
- **Charts**: `react-native-chart-kit`
- **Networking**: `axios`
- **Responsiveness**: `react-native-responsive-screen` or standard Flexbox.
- **Testing**: `jest`, `react-test-renderer`, `@testing-library/react-native` (Mocked).

### Features
1. **Auto-Location**: Request and retrieve user coordinates on startup.
2. **Dashboard**: Show current air quality index (AQI) or key pollutants.
3. **Charts**: Visualize hourly air quality and daily climate trends.
4. **Filters**: 
   - Select specific pollutants (PM10, PM2.5, etc.).
   - Select climate models.
   - Date range selection for climate.
5. **UI/UX**: Clean, modern interface with platform-specific adjustments for iOS/Android.

## Implementation Plan
1. Initialize Expo project in `mobile/`.
2. Define Folder Structure:
   - `src/models/`
   - `src/views/`
   - `src/controllers/`
   - `src/services/` (API client)
   - `src/components/` (Reusable UI)
3. Implement API Service.
4. Implement Location Controller.
5. Implement Views and Charts.
6. Add Tests.
