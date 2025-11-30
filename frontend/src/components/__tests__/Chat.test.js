import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import Chat from '../Chat';
import axios from 'axios';
import * as AuthContext from '../../contexts/AuthContext';

jest.mock('axios');
jest.mock('react-leaflet', () => ({
  MapContainer: ({ children }) => <div>{children}</div>,
  TileLayer: () => <div />,
  Marker: () => <div />,
  Popup: () => <div />,
  Polyline: () => <div />,
}));
jest.mock('../../contexts/AuthContext');

test('renders chat component and handles messages', async () => {
  const mockGetIdToken = jest.fn(() => Promise.resolve('test_token'));
  jest.spyOn(AuthContext, 'useAuth').mockImplementation(() => ({
    currentUser: { getIdToken: mockGetIdToken },
  }));

  axios.post.mockResolvedValue({
    data: {
      response: 'Hello!',
      session_id: '123',
      structured_data: { destination: 'Paris' },
    },
  });

  render(<Chat />);

  const input = screen.getByRole('textbox');
  const sendButton = screen.getByRole('button', { name: /send/i });

  fireEvent.change(input, { target: { value: 'Hi' } });
  fireEvent.click(sendButton);

  await waitFor(() => {
    expect(screen.getByText('Hi')).toBeInTheDocument();
  });

  await waitFor(() => {
    expect(screen.getByText('Hello!')).toBeInTheDocument();
  });

  expect(screen.getByTestId('travel-chip-destination')).toHaveTextContent('Destination: Paris');
});
