import React from 'react';
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <nav className="bg-gray-800 shadow-lg">
      <div className="max-w-7xl mx-auto px-4">
        <div className="flex justify-between h-16">
          <div className="flex">
            <div className="flex-shrink-0 flex items-center">
              <Link to="/">
                <span className="text-2xl font-bold text-emerald-500">StockPulse</span>
              </Link>
            </div>
            <div className="hidden md:ml-6 md:flex md:space-x-8">
              <Link to="/login" 
                className="inline-flex items-center px-1 pt-1 text-sm font-medium text-gray-100 hover:text-emerald-400"
              >
                Login
              </Link>
              <Link to="/register" 
                className="inline-flex items-center px-1 pt-1 text-sm font-medium text-gray-100 hover:text-emerald-400"
              >
                Register
              </Link>
              <Link to="http://localhost:8501" 
                className="inline-flex items-center px-1 pt-1 text-sm font-medium text-gray-100 hover:text-emerald-400"
              >
                Stock Analysis
              </Link>
              <Link to="http://localhost:8052" 
                className="inline-flex items-center px-1 pt-1 text-sm font-medium text-gray-100 hover:text-emerald-400"
              >
                News Analysis
              </Link>
            </div>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;