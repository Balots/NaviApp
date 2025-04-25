// src/App.js
import React, { useEffect, useState } from 'react';
import MapComponent from './components/Map';
import PlaceList from './components/PlaceList';
import PlaceDetail from './components/PlaceDetail';
import { fetchPlaces, searchPlaces } from './services/api';

function App() {
    const [places, setPlaces] = useState([]);
    const [selectedPlace, setSelectedPlace] = useState(null);
    const [query, setQuery] = useState('');

    useEffect(() => {
        const getPlaces = async () => {
            const data = await fetchPlaces();
            setPlaces(data);
        };

        getPlaces();
    }, []);

    const handleSearch = async () => {
        const data = await searchPlaces(query);
        setPlaces(data);
    };

    return (
        <div>
            <h1>Приложение для поиска мест</h1>
            <input
                type="text"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                placeholder="Введите запрос"
            />
            <button onClick={handleSearch}>Поиск</button>
            <MapComponent places={places} />
            <PlaceList places={places} />
            {selectedPlace && <PlaceDetail place={selectedPlace} />}
        </div>
    );
}

export default App;
