import React from 'react';
import { render, screen } from '@testing-library/react';
import LoginModal from '../LoginModal';
import * as AuthContext from '../../contexts/AuthContext';

jest.mock('axios');

test('renders login modal', () => {
  const contextValues = {
    login: jest.fn(),
    signup: jest.fn(),
    loginWithGoogle: jest.fn(),
  };

  jest.spyOn(AuthContext, 'useAuth').mockImplementation(() => contextValues);

  render(<LoginModal isOpen={true} />);
  expect(screen.getByRole('heading', { name: /login/i })).toBeInTheDocument();
});
