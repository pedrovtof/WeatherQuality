export interface WeatherParams {
  latitude: number;
  longitude: number;
  hourly?: string[];
}

export interface ClimateParams {
  latitude: number;
  longitude: number;
  start_date: string;
  end_date: string;
  models: string[];
  daily?: string[];
}

export interface AirQualityData {
  time: string[];
  [key: string]: number[] | string[];
}

export interface ClimateData {
  Model: string;
  Daily: {
    time: string[];
    [key: string]: number[] | string[];
  };
}

export interface ApiResponse<T> {
  message: string;
  data: T;
}

export interface ClimateModel {
  model: string;
  description: string;
}
