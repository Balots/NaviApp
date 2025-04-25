// src/components/Map.js
import React, { useEffect, useState } from 'react';
import { YMaps, Map, Placemark } from 'react-yandex-maps';

const MapComponent = ({ places }) => {
    const defaultState = { center: [56.838664, 60.604135], zoom: 13 };

    return (
        <YMaps>
            <Map defaultState={defaultState} width="100%" height="800px">
                {places.map((place) => (
                    <Placemark
                        key={place.id}
                        geometry={[place.latitude]}
                        properties={{
                            iconCaption: place.name,
                        }}
                    />
                ))}
            </Map>
        </YMaps>
    );
};

export default MapComponent;
