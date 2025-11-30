import React, { useState } from 'react';
import Navbar from './components/Navbar';
import Chat from './components/Chat';
import SwapSuggestion from './components/SwapSuggestion';
import SavedItineraries from './components/SavedItineraries';
import { useAuth } from './contexts/AuthContext';
import axios from 'axios';

function App() {
  const { currentUser } = useAuth();
  const [swapData, setSwapData] = useState(null);
  const [savedItineraries, setSavedItineraries] = useState([]);

  const handleSwapRequest = async () => {
    const mockData = {
      original_poi: { name: 'Eiffel Tower', crowd_score: 90 },
      user_preferences: { travel_style: 'history', crowd_tolerance: 3 },
    };

    try {
      const response = await axios.post('/api/recommendations/alternatives', mockData);
      setSwapData({ original: mockData.original_poi, alternative: response.data });
    } catch (error) {
      console.error('Error getting swap suggestion:', error);
    }
  };

  const handleLoadSavedItineraries = async () => {
    try {
      const token = await currentUser.getIdToken();
      const response = await axios.get('/api/itinerary/user/saved', {
        headers: { Authorization: `Bearer ${token}` },
      });
      setSavedItineraries(response.data);
    } catch (error) {
      console.error('Error loading saved itineraries:', error);
    }
  };

  return (
    <div className="App">
      <Navbar />
      <div className="p-4">
        {currentUser ? (
          <>
            <Chat />
            <button
              onClick={handleSwapRequest}
              className="bg-yellow-500 text-white p-2 rounded mt-4"
            >
              Get Swap Suggestion (Test)
            </button>
            <button
              onClick={handleLoadSavedItineraries}
              className="bg-indigo-500 text-white p-2 rounded mt-4 ml-2"
            >
              View Saved Itineraries
            </button>
            <SwapSuggestion original={swapData?.original} alternative={swapData?.alternative} />
            <SavedItineraries itineraries={savedItineraries} />
          </>
        ) : (
          <p className="text-center">Please log in to start a conversation.</p>
        )}
      </div>
    </div>
  );
}

export default App;
