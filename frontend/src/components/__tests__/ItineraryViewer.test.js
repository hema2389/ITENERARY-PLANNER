import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import ItineraryViewer from '../ItineraryViewer';
import * as AuthContext from '../../contexts/AuthContext';
import axios from 'axios';

jest.mock('axios');

const mockItinerary = {
  destination: 'Paris',
  days: [{ day_number: 1, activities: [{ name: 'Eiffel Tower' }] }],
};

test('renders itinerary viewer and handles PDF download', async () => {
  const mockGetIdToken = jest.fn(() => Promise.resolve('test_token'));
  jest.spyOn(AuthContext, 'useAuth').mockImplementation(() => ({
    currentUser: { getIdToken: mockGetIdToken },
  }));

  axios.post.mockResolvedValue({ data: new Blob() });

  // Mock URL.createObjectURL
  window.URL.createObjectURL = jest.fn(() => 'mock-url');

  render(<ItineraryViewer itinerary={mockItinerary} />);

  fireEvent.click(screen.getByText(/Download PDF/i));

  await waitFor(() => {
    expect(axios.post).toHaveBeenCalledWith('/api/export/pdf', mockItinerary, {
      responseType: 'blob',
    });
  });
});
