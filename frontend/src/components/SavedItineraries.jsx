import React from 'react';

const SavedItineraries = ({ itineraries }) => {
  if (!itineraries || itineraries.length === 0) return null;

  return (
    <div className="saved-itineraries mt-4">
      <h2 className="text-2xl font-bold mb-4">Your Saved Itineraries</h2>
      {itineraries.map((itinerary) => (
        <div key={itinerary.itinerary_id} className="border p-4 mb-2 rounded">
          <h3 className="font-bold">{itinerary.destination}</h3>
          {/* In a real app, you would display more details here */}
        </div>
      ))}
    </div>
  );
};

export default SavedItineraries;
