import React from 'react';
import { render } from '@testing-library/react';
import Map from '../Map';

// Mock react-leaflet
jest.mock('react-leaflet', () => ({
  MapContainer: ({ children }) => <div>{children}</div>,
  TileLayer: () => <div />,
  Marker: () => <div />,
  Popup: () => <div />,
  Polyline: () => <div />,
}));

test('renders map component', () => {
  render(<Map />);
});
