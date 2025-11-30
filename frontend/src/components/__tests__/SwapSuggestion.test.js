import React from 'react';
import { render, screen } from '@testing-library/react';
import SwapSuggestion from '../SwapSuggestion';

test('renders swap suggestion component', () => {
  const original = { name: 'Eiffel Tower', crowd_score: 90 };
  const alternative = { name: 'Colmar, France', average_crowd_density: 40, sustainability_score: 80 };

  render(<SwapSuggestion original={original} alternative={alternative} />);

  expect(screen.getByText(/Eiffel Tower/i)).toBeInTheDocument();
  expect(screen.getByText(/Colmar, France/i)).toBeInTheDocument();
  expect(screen.getByText(/Crowd Score: 40/i)).toBeInTheDocument();
});
