import React, { useState } from 'react';
import axios from 'axios';
import TravelChip from './TravelChip';

const Chat = () => {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');
  const [sessionId, setSessionId] = useState(null);
  const [structuredData, setStructuredData] = useState({});

  const handleSendMessage = async () => {
    if (input.trim() === '') return;

    const userMessage = { text: input, sender: 'user' };
    setMessages((prevMessages) => [...prevMessages, userMessage]);
    setInput('');

    try {
      const response = await axios.post('/api/chat/message', {
        message: input,
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
      <div className="input-area mt-4 flex">
        <input
          type="text"
          className="flex-grow border rounded-l p-2"
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyPress={(e) => e.key === 'Enter' && handleSendMessage()}
        />
        <button
          onClick={handleSendMessage}
          className="bg-blue-500 text-white p-2 rounded-r"
        >
          Send
        </button>
      </div>
    </div>
  );
};

export default Chat;
