// src/components/PlaceDetail.js
import React from 'react';

const PlaceDetail = ({ place }) => {
    return (
        <div>
            <h2>{place.name}</h2>
            <p>Адрес: {place.address}</p>
            <p>Категория: {place.category}</p>
            <p>Рейтинг: {place.rating}</p>
            <p>Описание: {place.description}</p>
        </div>
    );
};

export default PlaceDetail;
