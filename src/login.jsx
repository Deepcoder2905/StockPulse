import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

function Login() {
  const navigate = useNavigate();
  const [form, setForm] = useState({ username: '', password: '' });
  const [message, setMessage] = useState('');

  const handleChange = e => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async e => {
    e.preventDefault();
    try {
      const response = await axios.post('/login', form);
      setMessage(response.data.message);
      if (response.status === 200) {
        navigate('/');
      }
    } catch (error) {
      if (error.response && error.response.data) {
        setMessage(error.response.data.message);
      } else {
        setMessage('An error occurred.');
      }
    }
  };

  return (
    <div className="max-w-md mx-auto bg-gray-800 rounded-lg shadow-lg p-8">
      <h2 className="text-3xl font-bold text-center mb-8 text-emerald-500">Login</h2>
      {message && (
        <div className="mb-4 p-4 rounded bg-gray-700 text-gray-100">
          {message}
        </div>
      )}
      <form onSubmit={handleSubmit} className="space-y-6">
        <div>
          <label className="block text-sm font-medium text-gray-300 mb-2">
            Username
          </label>
          <input
            type="text"
            name="username"
            value={form.username}
            onChange={handleChange}
            required
            className="w-full px-4 py-2 rounded bg-gray-700 border border-gray-600 text-gray-100 focus:outline-none focus:border-emerald-500"
          />
        </div>
        <div>
          <label className="block text-sm font-medium text-gray-300 mb-2">
            Password
          </label>
          <input
            type="password"
            name="password"
            value={form.password}
            onChange={handleChange}
            required
            className="w-full px-4 py-2 rounded bg-gray-700 border border-gray-600 text-gray-100 focus:outline-none focus:border-emerald-500"
          />
        </div>
        <button
          type="submit"
          className="w-full bg-emerald-600 text-white py-2 px-4 rounded hover:bg-emerald-700 focus:outline-none focus:ring-2 focus:ring-emerald-500 focus:ring-offset-2 focus:ring-offset-gray-800"
        >
          Login
        </button>
      </form>
    </div>
  );
}

export default Login;
