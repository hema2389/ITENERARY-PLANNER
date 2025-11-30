import React, { useState } from 'react';
import axios from 'axios';
import TravelChip from './TravelChip';
import SuggestionChip from './SuggestionChip';
import ItineraryViewer from './ItineraryViewer';

const Chat = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [sessionId, setSessionId] = useState(null);
  const [structuredData, setStructuredData] = useState({});
  const [itinerary, setItinerary] = useState(null);

  const handleSendMessage = async (messageText = input) => {
    if (messageText.trim() === '') return;

    const userMessage = { text: messageText, sender: 'user' };
    setMessages((prevMessages) => [...prevMessages, userMessage]);
    setInput('');

    try {
      const response = await axios.post('/api/chat/message', {
        message: messageText,
        session_id: sessionId,
      });

      const aiMessage = { text: response.data.response, sender: 'ai' };
      setMessages((prevMessages) => [...prevMessages, aiMessage]);
      setSessionId(response.data.session_id);
      setStructuredData(response.data.structured_data);
    } catch (error) {
      console.error('Error sending message:', error);
    }
  };

  const handleSuggestionClick = (suggestion) => {
    setInput(suggestion);
    handleSendMessage(suggestion);
  };

  const suggestions = ["Plan a trip to Paris", "I want to go to the mountains", "I'm looking for a relaxing beach vacation"];

  const showMockItinerary = () => {
    setItinerary({
        days: [
            { day_number: 1, activities: [{name: "Eiffel Tower", description: "Visit the iconic tower.", reason: "low crowd score"}] },
            { day_number: 2, activities: [{name: "Louvre", description: "See the Mona Lisa.", reason: "authentic experience"}] }
        ]
    });
  };

  return (
    <div className="chat-container p-4">
      <div className="structured-data-area mb-4 flex flex-wrap">
        <TravelChip label="Destination" value={structuredData.destination} />
        <TravelChip label="Dates" value={structuredData.dates} />
        <TravelChip label="Budget" value={structuredData.budget} />
        <TravelChip label="Style" value={structuredData.travel_style} />
        <TravelChip label="Crowd Tolerance" value={structuredData.crowd_tolerance} />
      </div>
      <div className="messages-area border rounded p-4 h-96 overflow-y-auto">
        {messages.map((msg, index) => (
          <div key={index} className={`message p-2 my-1 rounded ${
            msg.sender === 'user' ? 'bg-blue-200 text-right ml-auto' : 'bg-gray-200 text-left mr-auto'
          }`}
          style={{width: 'fit-content', maxWidth: '70%'}}>
            {msg.text}
          </div>
        ))}
      </div>
      <div className="suggestions-area mt-4 flex flex-wrap">
        {messages.length === 0 && suggestions.map((suggestion, index) => (
          <SuggestionChip key={index} suggestion={suggestion} onClick={handleSuggestionClick} />
        ))}
      </div>
      <div className="input-area mt-4 flex">
        <input
          type="text"
          className="flex-grow border rounded-l p-2"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' && handleSendMessage()}
        />
        <button
          onClick={() => handleSendMessage()}
          className="bg-blue-500 text-white p-2 rounded-r"
        >
          Send
        </button>
      </div>
      <button onClick={showMockItinerary} className="bg-purple-500 text-white p-2 rounded mt-4">
        Show Mock Itinerary
      </button>
      <ItineraryViewer itinerary={itinerary} />
    </div>
  );
};

export default Chat;
