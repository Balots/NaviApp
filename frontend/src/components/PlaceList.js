// src/components/PlaceList.js
import React from 'react';

const PlaceList = ({ places }) => {
    return (
        <div>
            <h2>Список мест</h2>
            <ul>
                {places.map((place) => (
                    <li key={place.id}>{place.name}</li>
                ))}
            </ul>
        </div>
    );
};

export default PlaceList;
