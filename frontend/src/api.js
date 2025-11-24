import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export const scrapeBatch = async (url, maxPages = 5) => {
  const response = await api.post('/api/scrape-batch', { url, max_pages: maxPages });
  return response.data;
};

export const getStats = async () => {
  const response = await api.get('/api/stats');
  return response.data;
};

export const scrapeSingle = async (url) => {
  const response = await api.post('/api/scrape-single', { url });
  return response.data;
};

export const getProducts = async (skip = 0, limit = 100) => {
  const response = await api.get('/api/products', { params: { skip, limit } });
  return response.data;
};

export const clearProducts = async () => {
  const response = await api.delete('/api/products/clear');
  return response.data;
};

export default api;
