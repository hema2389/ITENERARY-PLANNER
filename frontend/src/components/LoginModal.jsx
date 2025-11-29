import React, { useState } from 'react';
import { useAuth } from '../contexts/AuthContext';

const LoginModal = ({ isOpen, onClose }) => {
  const { login, signup, loginWithGoogle } = useAuth();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');

  const handleLogin = async () => {
    try {
      await login(email, password);
      onClose();
    } catch (err) {
      setError('Failed to log in');
    }
  };

  const handleSignup = async () => {
    try {
      await signup(email, password);
      onClose();
    } catch (err) {
      setError('Failed to sign up');
    }
  };

  const handleGoogleSignIn = async () => {
    try {
      await loginWithGoogle();
      onClose();
    } catch (err) {
      setError('Failed to sign in with Google');
    }
  };

  if (!isOpen) return null;

  return (
    <div className="fixed inset-0 bg-gray-600 bg-opacity-50 overflow-y-auto h-full w-full flex items-center justify-center">
      <div className="p-8 border w-96 shadow-lg rounded-md bg-white">
        <div className="text-center">
          <h3 className="text-2xl font-bold text-gray-900">Login</h3>
          {error && <p className="text-red-500">{error}</p>}
          <div className="mt-4">
            <input
              type="email"
              placeholder="Email"
              className="w-full p-2 border border-gray-300 rounded mt-2"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
            />
            <input
              type="password"
              placeholder="Password"
              className="w-full p-2 border border-gray-300 rounded mt-2"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
            />
          </div>
          <div className="mt-6">
            <button onClick={handleLogin} className="w-full p-2 bg-blue-500 text-white rounded">
              Login
            </button>
            <button onClick={handleSignup} className="w-full p-2 bg-green-500 text-white rounded mt-2">
              Sign Up
            </button>
            <button onClick={handleGoogleSignIn} className="w-full p-2 bg-red-500 text-white rounded mt-2">
              Sign in with Google
            </button>
          </div>
          <div className="mt-4">
            <button onClick={onClose} className="text-sm text-gray-500">
              Close
            </button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default LoginModal;
