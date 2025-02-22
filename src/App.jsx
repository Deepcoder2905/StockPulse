import React from 'react';
import { Routes, Route } from 'react-router-dom';
import Navbar from './navbar';
import Home from './Home';
import Login from './Login';
import Register from './Register';
import StockAnalysis from './StockAnalysis'; 
// import NewsAnalysis from './NewsAnalysis';

function App() {
  return (
    <div className="min-h-screen bg-gray-900 text-gray-100">
      <Navbar />
      <main className="max-w-7xl mx-auto py-6 sm:px-6 lg:px-8">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/login" element={<Login />} />
          <Route path="/register" element={<Register />} />
          <Route path="/stock-analysis" element={<StockAnalysis />} />
          {/* <Route path="/news-analysis" element={<NewsAnalysis />} />  */}
        </Routes>
      </main>
    </div>
  );
}

export default App;