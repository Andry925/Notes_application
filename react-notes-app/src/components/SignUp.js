import React, { useState } from 'react';
import axios from 'axios'; // Import axios

function RegistrationPage() {
  const [formData, setFormData] = useState({
    username: '',
    email: '',
    password: ''
  });

  const handleChange = (event) => {
    const { name, value } = event.target;
    setFormData(prevState => ({
      ...prevState,
      [name]: value
    }));
  };

  const handleSubmit = (event) => {
    event.preventDefault()
    axios.post('http://localhost:8000/api/register/', formData)
      .then(response => {
        console.log('Registration successful:', response.data);
      })
      .catch(error => {
        console.error('Error registering:', error);

      });
  };

  return (
    <div style={{ display: 'flex', justifyContent: 'center', marginTop: '50px' }}>
      <form onSubmit={handleSubmit} style={{ width: '300px' }}>
        <h2 style={{ textAlign: 'center' }}>Sign Up</h2>
        <div style={{ marginBottom: '20px' }}>
          <label htmlFor="username" style={{ display: 'block' }}>Username:</label>
          <input
            type="text"
            id="username"
            name="username"
            value={formData.username}
            onChange={handleChange}
            required
            style={{ width: '100%', padding: '10px', margin: '5px 0 15px' }}
          />
        </div>
        <div style={{ marginBottom: '20px' }}>
          <label htmlFor="email" style={{ display: 'block' }}>Email:</label>
          <input
            type="email"
            id="email"
            name="email"
            value={formData.email}
            onChange={handleChange}
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
            value={formData.password}
            onChange={handleChange}
            required
            style={{ width: '100%', padding: '10px', margin: '5px 0 15px' }}
          />
        </div>
        <button type="submit" style={{ width: '100%', padding: '10px', backgroundColor: '#4CAF50', color: 'white', fontSize: '16px', cursor: 'pointer' }}>Register</button>
      </form>
    </div>
  );
}

export default RegistrationPage;
