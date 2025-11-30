import React from 'react';
import { MapContainer, TileLayer, Marker, Popup } from 'react-leaflet';

const Map = ({ pois }) => {
  const defaultCenter = [51.505, -0.09];
  const defaultZoom = 13;

  return (
    <MapContainer center={defaultCenter} zoom={defaultZoom} style={{ height: '400px', width: '100%' }}>
      <TileLayer
        url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
        attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
      />
      {pois && pois.map((poi, index) => (
        <Marker key={index} position={poi.coordinates}>
          <Popup>{poi.name}</Popup>
        </Marker>
      ))}
    </MapContainer>
  );
};

export default Map;
