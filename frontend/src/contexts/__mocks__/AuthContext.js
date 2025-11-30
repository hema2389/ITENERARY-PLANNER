import React from 'react';

export const useAuth = () => ({
  currentUser: { email: 'test@example.com', getIdToken: jest.fn(() => Promise.resolve('test_token')) },
});

export const AuthProvider = ({ children }) => {
  return <>{children}</>;
};
