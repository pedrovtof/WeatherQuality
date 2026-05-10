import apiClient from './apiClient';
import { ClimateParams, ApiResponse, ClimateData } from '../interfaces/ApiInterfaces';
import { CONFIG } from '../constants/Config';

export const ClimateService = {
  getClimateData: async (params: ClimateParams): Promise<ApiResponse<ClimateData[]>> => {
    const response = await apiClient.get(CONFIG.CLIMATE_ENDPOINT, { params });
    return response.data;
  },

  getModels: async (): Promise<ApiResponse<{ model: string; description: string }[]>> => {
    const response = await apiClient.get(CONFIG.CLIMATE_MODELS_ENDPOINT);
    return response.data;
  },
};
