import React from 'react';
import { render, screen } from '@testing-library/react';
import ItineraryViewer from '../ItineraryViewer';
import * as AuthContext from '../../contexts/AuthContext';
import axios from 'axios';

jest.mock('axios');
jest.mock('../../contexts/AuthContext');

const mockItinerary = {
  destination: 'Paris',
  days: [{ day_number: 1, activities: [{ name: 'Eiffel Tower' }] }],
};

test('renders itinerary viewer', () => {
  const mockGetIdToken = jest.fn(() => Promise.resolve('test_token'));
  jest.spyOn(AuthContext, 'useAuth').mockImplementation(() => ({
    currentUser: { getIdToken: mockGetIdToken },
  }));

  render(<ItineraryViewer itinerary={mockItinerary} />);
  expect(screen.getByText(/Your Itinerary/i)).toBeInTheDocument();
  expect(screen.getByText(/Day 1/i)).toBeInTheDocument();
});
