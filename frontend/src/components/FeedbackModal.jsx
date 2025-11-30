import React, { useState } from 'react';
import axios from 'axios';
import { useAuth } from '../contexts/AuthContext';

const FeedbackModal = ({ isOpen, onClose, itineraryId }) => {
  const { currentUser } = useAuth();
  const [satisfaction, setSatisfaction] = useState(0);
  const [quality, setQuality] = useState(0);
  const [comments, setComments] = useState('');

  const handleSubmit = async () => {
    try {
      const token = await currentUser.getIdToken();
      await axios.post('/api/itinerary/user/feedback', {
        itinerary_id: itineraryId,
        crowd_averse_satisfaction: satisfaction,
        experience_quality: quality,
        comments: comments,
      }, {
        headers: { Authorization: `Bearer ${token}` },
      });
      onClose();
    } catch (error) {
      console.error('Error submitting feedback:', error);
    }
  };

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full flex items-center justify-center">
      <div className="p-8 border w-96 shadow-lg rounded-md bg-white">
        <h3 className="text-2xl font-bold text-gray-900">Feedback</h3>
        <div className="mt-4">
          <label htmlFor="satisfaction" className="block">Crowd-Averse Satisfaction (1-5)</label>
          <input id="satisfaction" type="number" min="1" max="5" value={satisfaction} onChange={(e) => setSatisfaction(e.target.value)} className="w-full p-2 border" />
        </div>
        <div className="mt-4">
          <label htmlFor="quality" className="block">Experience Quality (1-5)</label>
          <input id="quality" type="number" min="1" max="5" value={quality} onChange={(e) => setQuality(e.target.value)} className="w-full p-2 border" />
        </div>
        <div className="mt-4">
          <label htmlFor="comments" className="block">Comments</label>
          <textarea id="comments" value={comments} onChange={(e) => setComments(e.target.value)} className="w-full p-2 border" />
        </div>
        <div className="mt-6 flex justify-between">
          <button onClick={handleSubmit} className="bg-blue-500 text-white p-2 rounded">Submit</button>
          <button onClick={onClose} className="text-sm text-gray-500">Close</button>
        </div>
      </div>
    </div>
  );
};

export default FeedbackModal;
