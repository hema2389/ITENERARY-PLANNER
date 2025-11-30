import React from 'react';

const SwapSuggestion = ({ original, alternative }) => {
  if (!original || !alternative) return null;

  return (
    <div className="swap-suggestion-container p-4 border rounded mt-4">
      <h2 className="text-xl font-bold mb-4">Swap Suggestion</h2>
      <div className="grid grid-cols-2 gap-4">
        <div>
          <h3 className="font-bold">{original.name}</h3>
          <p>Crowd Score: {original.crowd_score}</p>
        </div>
        <div>
          <h3 className="font-bold">{alternative.name}</h3>
          <p>Crowd Score: {alternative.average_crowd_density}</p>
          <p>Sustainability Score: {alternative.sustainability_score}</p>
          <button className="bg-green-500 text-white p-2 rounded mt-2">
            Swap
          </button>
        </div>
      </div>
    </div>
  );
};

export default SwapSuggestion;
