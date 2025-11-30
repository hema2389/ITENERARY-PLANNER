import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react';
import Chat from '../Chat';
import axios from 'axios';

jest.mock('axios');

test('renders chat component and handles messages', async () => {
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

  expect(screen.getByText((content, element) => {
    const hasText = (node) => node.textContent === 'Destination: Paris';
    const nodeHasText = hasText(element);
    const childrenDontHaveText = Array.from(element.children).every(
      (child) => !hasText(child)
    );
    return nodeHasText && childrenDontHaveText;
  })).toBeInTheDocument();
});
