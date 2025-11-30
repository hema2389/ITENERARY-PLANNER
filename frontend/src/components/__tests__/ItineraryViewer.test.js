import React from 'react';
import { render, screen, waitFor } from '@testing-library/react';
import ItineraryViewer from '../ItineraryViewer';
import * as AuthContext from '../../contexts/AuthContext';
import axios from 'axios';

jest.mock('axios');
jest.mock('react-leaflet', () => ({
  MapContainer: ({ children }) => <div>{children}</div>,
  TileLayer: () => <div />,
  Marker: () => <div />,
  Popup: () => <div />,
  Polyline: () => <div />,
}));
jest.mock('../../contexts/AuthContext');

const mockItinerary = {
  destination: 'Paris',
  days: [{ day_number: 1, activities: [{ name: 'Eiffel Tower' }] }],
};

test('renders itinerary viewer', async () => {
  const mockGetIdToken = jest.fn(() => Promise.resolve('test_token'));
  jest.spyOn(AuthContext, 'useAuth').mockImplementation(() => ({
    currentUser: { getIdToken: mockGetIdToken },
  }));

  axios.post.mockResolvedValue({ data: {} });

  render(<ItineraryViewer itinerary={mockItinerary} />);

  await waitFor(() => {
    expect(axios.post).toHaveBeenCalledWith('/api/maps/geodata', {
      locations: ['Eiffel Tower'],
    });
  });

  expect(screen.getByText(/Your Itinerary/i)).toBeInTheDocument();
  expect(screen.getAllByText(/Day 1/i).length).toBe(2);
});
