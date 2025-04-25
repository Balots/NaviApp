// src/services/api.js
import axios from 'axios';

const API_URL = 'http://127.0.0.1:8005';

export const fetchPlaces = async () => {
    const response = await axios.get(`${API_URL}/places/`);
    return response.data;
};

export const searchPlaces = async (query) => {
    const response = await axios.get(`${API_URL}/places/search/?query=${query}`);
    return response.data;
};
