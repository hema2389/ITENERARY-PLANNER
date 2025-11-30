import React from 'react';

const TravelChip = ({ label, value }) => {
  if (!value) return null;

  return (
    <div className="bg-gray-200 rounded-full px-3 py-1 text-sm font-semibold text-gray-700 mr-2 mb-2">
      <strong>{label}:</strong> {value}
    </div>
  );
};

export default TravelChip;
