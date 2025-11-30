import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import FeedbackModal from '../FeedbackModal';
import axios from 'axios';
import * as AuthContext from '../../contexts/AuthContext';

jest.mock('axios');
jest.mock('../../contexts/AuthContext');

test('renders feedback modal and submits feedback', async () => {
  const mockGetIdToken = jest.fn(() => Promise.resolve('test_token'));
  jest.spyOn(AuthContext, 'useAuth').mockImplementation(() => ({
    currentUser: { getIdToken: mockGetIdToken },
  }));

  const onClose = jest.fn();

  render(<FeedbackModal isOpen={true} itineraryId="123" onClose={onClose} />);

  fireEvent.change(screen.getByLabelText(/Crowd-Averse Satisfaction/i), { target: { value: '5' } });
  fireEvent.click(screen.getByText(/Submit/i));

  await waitFor(() => {
    expect(axios.post).toHaveBeenCalledWith('/api/itinerary/user/feedback', {
      itinerary_id: '123',
      crowd_averse_satisfaction: '5',
      experience_quality: 0,
      comments: '',
    }, {
      headers: { Authorization: 'Bearer test_token' },
    });
  });
});
