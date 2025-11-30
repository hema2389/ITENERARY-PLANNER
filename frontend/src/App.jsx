import React from 'react';
import Navbar from './components/Navbar';
import Chat from './components/Chat';
import { useAuth } from './contexts/AuthContext';

function App() {
  const { currentUser } = useAuth();

  return (
    <div className="App">
      <Navbar />
      <div className="p-4">
        {currentUser ? (
          <Chat />
        ) : (
          <p className="text-center">Please log in to start a conversation.</p>
        )}
      </div>
    </div>
  );
}

export default App;
