import React, { useEffect, useState } from 'react';
import MapComponent from './components/Map';
import PlaceList from './components/PlaceList';
import { fetchPlaces, searchPlaces } from './services/api';

function App() {
    const [places, setPlaces] = useState([]);
    const [query, setQuery] = useState('');

    useEffect(() => {
        const getPlaces = async () => {
            try {
                const data = await fetchPlaces();
                setPlaces(data);
            } catch (error) {
                console.error("Error fetching places:", error);
            }
        };

        getPlaces();
    }, []);

    const handleSearch = async () => {
        try {
            const data = await searchPlaces(query);
            setPlaces(data);
        } catch (error) {
            console.error("Error searching places:", error);
        }
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
        </div>
    );
}

export default App;
