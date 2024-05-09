import React, { useState, useEffect } from 'react';
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import NotesList from './components/NotesList';
import Search from './components/Search';
import Header from './components/Header';
import RegistrationPage from './components/SignUp';
import LoginPage from './components/Login';
import SignUp from "./components/SignUp";

const App = () => {
  const [notes, setNotes] = useState([
    {
      id: '1',
      text: 'This is my first note!',
      date: '15/04/2021',
    },
    {
      id: '2',
      text: 'This is my second note!',
      date: '21/04/2021',
    },
    {
      id: '3',
      text: 'This is my third note!',
      date: '28/04/2021',
    },
    {
      id: '4',
      text: 'This is my new note!',
      date: '30/04/2021',
    },
  ]);

  const [searchText, setSearchText] = useState('');
  const [darkMode, setDarkMode] = useState(false);

  useEffect(() => {
    const savedNotes = JSON.parse(
      localStorage.getItem('react-notes-app-data')
    );

    if (savedNotes) {
      setNotes(savedNotes);
    }
  }, []);

  useEffect(() => {
    localStorage.setItem(
      'react-notes-app-data',
      JSON.stringify(notes)
    );
  }, [notes]);

  const addNote = (text) => {
    const date = new Date();
    const newNote = {
      id: 1,
      text: text,
      date: date.toLocaleDateString(),
    };
    const newNotes = [...notes, newNote];
    setNotes(newNotes);
  };

  const deleteNote = (id) => {
    const newNotes = notes.filter((note) => note.id !== id);
    setNotes(newNotes);
  };

 return (
    <BrowserRouter>
      <div className={`${darkMode ? 'dark-mode' : ''}`}>
        <div className='container'>
          <Header handleToggleDarkMode={setDarkMode} />
          <Routes>
            <Route path="/" element={< SignUp/>} />
            <Route path="/register" element={<RegistrationPage />} />
            <Route path="/login" element={<LoginPage />} />
            <Route path="/home" element={
              <>
                <Search handleSearchNote={setSearchText} />
                <NotesList
                  notes={notes.filter(note => note.text.toLowerCase().includes(searchText))}
                />
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