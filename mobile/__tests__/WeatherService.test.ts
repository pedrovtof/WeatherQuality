import { WeatherService } from '../src/services/WeatherService';
import apiClient from '../src/services/apiClient';

jest.mock('../src/services/apiClient');

describe('WeatherService', () => {
  it('fetches air quality data successfully', async () => {
    const mockData = {
      message: 'Sucess',
      data: {
        Hourly: {
          time: ['2024-05-10T12:00'],
          pm10: [10.5],
        },
      },
    };

    (apiClient.get as jest.Mock).mockResolvedValue({ data: mockData });

    const params = { latitude: 52.52, longitude: 13.41, hourly: ['pm10'] };
    const result = await WeatherService.getAirQuality(params);

    expect(result).toEqual(mockData);
    expect(apiClient.get).toHaveBeenCalledWith('/weather', { params });
  });
});
