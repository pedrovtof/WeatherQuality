import apiClient from './apiClient';
import { WeatherParams, ApiResponse, AirQualityData } from '../interfaces/ApiInterfaces';
import { CONFIG } from '../constants/Config';

export const WeatherService = {
  getAirQuality: async (params: WeatherParams): Promise<ApiResponse<{ Hourly: AirQualityData }>> => {
    // Axios handles array params by repeating the key: hourly=pm10&hourly=pm2_5
    const response = await apiClient.get(CONFIG.WEATHER_ENDPOINT, { params });
    return response.data;
  },
};
