import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';


function LoginPage() {
  const navigate = useNavigate();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleLogin = (event) => {
    event.preventDefault();
    axios.post('http://localhost:8000/api/login/', { email, password })
      .then(response => {
        console.log('Login successful', response.data);
        localStorage.setItem('token', response.data.token);
        alert('You are logged in!');
        navigate('/home');
      })
      .catch(error => {
        console.error('Login failed:', error.response.data);
        alert('Login failed!');
      });
  };

  return (
    <div style={{ display: 'flex', justifyContent: 'center', marginTop: '50px' }}>
      <form onSubmit={handleLogin} style={{ width: '300px' }}>
        <h2 style={{ textAlign: 'center' }}>Login</h2>
        <div style={{ marginBottom: '20px' }}>
          <label htmlFor="email" style={{ display: 'block' }}>Email:</label>
          <input
            type="email"
            id="email"
            name="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
            style={{ width: '100%', padding: '10px', margin: '5px 0 15px' }}
          />
        </div>
        <div style={{ marginBottom: '20px' }}>
          <label htmlFor="password" style={{ display: 'block' }}>Password:</label>
          <input
            type="password"
            id="password"
            name="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
            style={{ width: '100%', padding: '10px', margin: '5px 0 15px' }}
          />
        </div>
        <button type="submit" style={{ width: '100%', padding: '10px', backgroundColor: '#4CAF50', color: 'white', fontSize: '16px', cursor: 'pointer' }}>Login</button>
      </form>
    </div>
  );
}

export default LoginPage;
