import React, { useState } from 'react';
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import NotesManager from './components/NotesManager';
import Note from './components/Note'
import Search from './components/Search';
import Header from './components/Header';
import RegistrationPage from './components/SignUp';
import LoginPage from './components/Login';
import SignUp from "./components/SignUp";

const App = () => {
  const [searchText, setSearchText] = useState('');
  const [darkMode, setDarkMode] = useState(false);

  return (
    <BrowserRouter>
      <div className={`${darkMode ? 'dark-mode' : ''}`}>
        <div className='container'>
          <Header handleToggleDarkMode={setDarkMode} />
          <Routes>
            <Route path="/" element={<SignUp />} />
            <Route path="/register" element={<RegistrationPage />} />
            <Route path="/login" element={<LoginPage />} />
            <Route path="/home" element={
              <>
                <Search handleSearchNote={setSearchText} />
                <NotesManager searchText={searchText} />
              </>
            } />
            {/* Redirect any unknown paths back to register or login */}
            <Route path="*" element={<SignUp />} />
          </Routes>
        </div>
      </div>
    </BrowserRouter>
  );
};

export default App;
