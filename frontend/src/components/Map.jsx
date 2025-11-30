import React, { useState } from 'react';
import { MapContainer, TileLayer, Marker, Popup, Polyline } from 'react-leaflet';

const Map = ({ pois, days, geoData }) => {
  const [selectedDay, setSelectedDay] = useState(1);
  const defaultCenter = [48.8566, 2.3522]; // Paris center

  const dayRoutes = days ? days.map(day =>
    day.activities.map(activity => geoData?.coordinates[activity.name]).filter(coord => coord)
  ) : [];

  return (
    <div>
      <div className="day-selector my-2">
        {days && days.map(day => (
          <button
            key={day.day_number}
            onClick={() => setSelectedDay(day.day_number)}
            className={`p-2 mx-1 rounded ${selectedDay === day.day_number ? 'bg-blue-500 text-white' : 'bg-gray-200'}`}
          >
            Day {day.day_number}
          </button>
        ))}
      </div>
      <MapContainer center={defaultCenter} zoom={12} style={{ height: '400px', width: '100%' }}>
        <TileLayer
          url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          attribution='&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
        />
        {pois && pois.map((poi, index) => (
          poi.coordinates && <Marker key={index} position={poi.coordinates}>
            <Popup>{poi.name}</Popup>
          </Marker>
        ))}
        {dayRoutes[selectedDay - 1] && <Polyline positions={dayRoutes[selectedDay - 1]} color="blue" />}
      </MapContainer>
    </div>
  );
};

export default Map;
