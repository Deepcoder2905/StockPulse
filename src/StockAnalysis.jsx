import React from 'react';

const StockAnalysis = () => {
  return (
    <div style={{ height: '100vh' }}>
      <iframe 
        src="http://localhost:8501" 
        style={{ width: '100%', height: '100%', border: 'none' }}
        title="Stock Analysis App"
      />
    </div>
  );
};

export default StockAnalysis;
