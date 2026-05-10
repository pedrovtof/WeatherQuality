import { renderHook, act } from '@testing-library/react-native';
import { useAppController } from '../src/controllers/AppController';
import { WeatherService } from '../src/services/WeatherService';
import { ClimateService } from '../src/services/ClimateService';
import { LocationController } from '../src/controllers/LocationController';

jest.mock('../src/services/WeatherService');
jest.mock('../src/services/ClimateService');
jest.mock('../src/controllers/LocationController');

describe('AppController', () => {
  it('fetches location and data correctly', async () => {
    const mockLocation = { latitude: 10, longitude: 20 };
    (LocationController.getCurrentLocation as jest.Mock).mockResolvedValue(mockLocation);

    (WeatherService.getAirQuality as jest.Mock).mockResolvedValue({
      data: { Hourly: { time: ['12:00'], pm10: [5] } }
    });

    (ClimateService.getClimateData as jest.Mock).mockResolvedValue({
      data: [{ Model: 'MockModel', Daily: { time: ['May 10'], temperature_2m_max: [25] } }]
    });

    (ClimateService.getModels as jest.Mock).mockResolvedValue({
      data: [{ model: 'CMCC_CM2_VHR4', description: 'desc' }]
    });

    const { result } = renderHook(() => useAppController());

    await act(async () => {
      await result.current.fetchData();
    });

    expect(result.current.location).toEqual(mockLocation);
    expect(result.current.weatherData).toBeDefined();
    expect(result.current.climateData).toBeDefined();
    expect(result.current.loading).toBe(false);
  });

  it('handles errors gracefully', async () => {
    (LocationController.getCurrentLocation as jest.Mock).mockRejectedValue(new Error('Location Error'));

    const { result } = renderHook(() => useAppController());

    await act(async () => {
      await result.current.fetchData();
    });

    expect(result.current.error).toBe('Location Error');
    expect(result.current.loading).toBe(false);
  });
});
