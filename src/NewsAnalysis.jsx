// NewsAnalysis.jsx
import React from 'react';

const NewsAnalysis = () => {
  return (
    <div style={{ height: '100vh' }}>
      <iframe
        src="http://localhost:8502" // URL of your Streamlit news analysis app
        style={{ width: '100%', height: '100%', border: 'none' }}
        title="News Analysis App"
      />
    </div>
  );
};

export default NewsAnalysis;
