import React, { useState } from 'react';
import axios from 'axios';
import { useAuth } from '../contexts/AuthContext';
import FeedbackModal from './FeedbackModal';

const ItineraryViewer = ({ itinerary }) => {
  const { currentUser } = useAuth();
  const [openDay, setOpenDay] = useState(null);
  const [isSaved, setIsSaved] = useState(false);
  const [isFeedbackModalOpen, setIsFeedbackModalOpen] = useState(false);
  const [savedItineraryId, setSavedItineraryId] = useState(null);

  const toggleDay = (dayNumber) => {
    setOpenDay(openDay === dayNumber ? null : dayNumber);
  };

  const handleSaveItinerary = async () => {
    try {
      const token = await currentUser.getIdToken();
      const response = await axios.post('/api/itinerary/user/save', itinerary, {
        headers: { Authorization: `Bearer ${token}` },
      });
      setIsSaved(true);
      setSavedItineraryId(response.data.itinerary_id);
      setIsFeedbackModalOpen(true); // Open feedback modal on successful save
    } catch (error) {
      console.error('Error saving itinerary:', error);
    }
  };

  if (!itinerary) return null;

  return (
    <>
      <div className="itinerary-viewer mt-4">
        <h2 className="text-2xl font-bold mb-4">Your Itinerary</h2>
        {itinerary.days.map((day) => (
          <div key={day.day_number} className="border-b">
            <button
              onClick={() => toggleDay(day.day_number)}
              className="w-full text-left p-4 font-bold"
            >
              Day {day.day_number}
            </button>
            {openDay === day.day_number && (
              <div className="p-4">
                {day.activities.map((activity, index) => (
                  <div key={index} className="mb-2">
                    <h3 className="font-bold">{activity.name}</h3>
                    <p>{activity.description}</p>
                    <p className="text-sm text-gray-500">{activity.reason}</p>
                  </div>
                ))}
                <button className="bg-blue-500 text-white p-2 rounded mt-2">
                  Regenerate Day
                </button>
              </div>
            )}
          </div>
        ))}
        <button
          onClick={handleSaveItinerary}
          className={`p-2 rounded mt-4 ${isSaved ? 'bg-gray-400' : 'bg-green-500 text-white'}`}
          disabled={isSaved}
        >
          {isSaved ? 'Saved!' : 'Save Itinerary'}
        </button>
      </div>
      <FeedbackModal
        isOpen={isFeedbackModalOpen}
        onClose={() => setIsFeedbackModalOpen(false)}
        itineraryId={savedItineraryId}
      />
    </>
  );
};

export default ItineraryViewer;
