import axios from 'axios';
import { CONFIG } from '../constants/Config';

const apiClient = axios.create({
  baseURL: CONFIG.API_BASE_URL,
  timeout: 10000,
});

export default apiClient;
