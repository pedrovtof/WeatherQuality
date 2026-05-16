import { useState, useCallback, useEffect } from 'react';
import { WeatherService } from '../services/WeatherService';
import { ClimateService } from '../services/ClimateService';
import { LocationController } from './LocationController';
import { AirQualityData, ClimateData, ClimateModel } from '../interfaces/ApiInterfaces';

export const useAppController = () => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [location, setLocation] = useState<{ latitude: number; longitude: number } | null>(null);
  const [weatherData, setWeatherData] = useState<AirQualityData | null>(null);
  const [climateData, setClimateData] = useState<ClimateData[] | null>(null);
  const [selectedPollutants, setSelectedPollutants] = useState<string[]>(['pm2_5', 'pm10', 'nitrogen_dioxide']);
  const [availableModels, setAvailableModels] = useState<ClimateModel[]>([]);
  const [selectedModels, setSelectedModels] = useState<string[]>(['CMCC_CM2_VHR4']);

  // Date state
  const formatDate = (date: Date) => date.toISOString().split('T')[0];
  const initialEnd = new Date();
  const initialStart = new Date();
  initialStart.setDate(initialStart.getDate() - 7);

  const [startDate, setStartDate] = useState(formatDate(initialStart));
  const [endDate, setEndDate] = useState(formatDate(initialEnd));

  const fetchModels = useCallback(async () => {
    try {
      const res = await ClimateService.getModels();
      setAvailableModels(res.data);
    } catch (err: any) {
      console.error('Failed to fetch models', err);
    }
  }, []);

  useEffect(() => {
    fetchModels();
  }, [fetchModels]);

  const fetchData = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const loc = await LocationController.getCurrentLocation();
      setLocation(loc);

      // Fetch Weather (Air Quality)
      const weatherRes = await WeatherService.getAirQuality({
        latitude: loc.latitude,
        longitude: loc.longitude,
        hourly: selectedPollutants,
        start_date: startDate,
        end_date: endDate,
      });
      setWeatherData(weatherRes.data.Hourly);

      // Fetch Climate
      const climateRes = await ClimateService.getClimateData({
        latitude: loc.latitude,
        longitude: loc.longitude,
        start_date: startDate,
        end_date: endDate,
        models: selectedModels,
        daily: ['temperature_2m_max', 'temperature_2m_min'],
      });
      setClimateData(climateRes.data);
    } catch (err: any) {
      setError(err.message || 'An error occurred');
    } finally {
      setLoading(false);
    }
  }, [selectedPollutants, selectedModels, startDate, endDate]);

  const toggleModel = (model: string) => {
    setSelectedModels(prev => {
      if (prev.includes(model)) {
        if (prev.length === 1) return prev; // Keep at least one
        return prev.filter(m => m !== model);
      }
      return [...prev, model];
    });
  };

  const updateDates = (start: string, end: string) => {
    const s = new Date(start);
    const e = new Date(end);
    
    if (isNaN(s.getTime()) || isNaN(e.getTime())) {
      setError('Invalid date format.');
      return;
    }

    const diffTime = Math.abs(e.getTime() - s.getTime());
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24));

    if (diffDays > 90) {
      setError('The maximum period allowed is 90 days.');
      return;
    }
    
    setStartDate(start);
    setEndDate(end);
  };

  return {
    loading,
    error,
    location,
    weatherData,
    climateData,
    selectedPollutants,
    setSelectedPollutants,
    availableModels,
    selectedModels,
    toggleModel,
    startDate,
    endDate,
    updateDates,
    fetchData,
  };
};
