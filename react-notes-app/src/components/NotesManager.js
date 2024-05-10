import React, { useState,useEffect } from 'react';
import axios from 'axios';
import { MdDeleteForever, MdEdit, MdSave } from 'react-icons/md';

const Note = ({ id, text, date, handleDeleteNote, handleUpdateNote }) => {
    const [editMode, setEditMode] = useState(false);
    const [editedText, setEditedText] = useState(text);

    const saveEdit = () => {
        handleUpdateNote(id, editedText);
        setEditMode(false);
    };

    return (
        <div className='note'>
            {editMode ? (
                <textarea
                    value={editedText}
                    onChange={(e) => setEditedText(e.target.value)}
                    className='edit-textarea'
                />
            ) : (
                <span>{text}</span>
            )}
            <div className='note-footer'>
                <small>{date}</small>
                {editMode ? (
                    <MdSave
                        onClick={saveEdit}
                        className='save-icon'
                        size='1.3em'
                    />
                ) : (
                    <>
                        <MdEdit
                            onClick={() => setEditMode(true)}
                            className='edit-icon'
                            size='1.3em'
                        />
                        <MdDeleteForever
                            onClick={() => handleDeleteNote(id)}
                            className='delete-icon'
                            size='1.3em'
                        />
                    </>
                )}
            </div>
        </div>
    );
};

const NotesManager = () => {
    const [notes, setNotes] = useState([]);
    const [loading, setLoading] = useState(false);

    useEffect(() => {
        const fetchNotes = async () => {
            const token = localStorage.getItem('token');
            setLoading(true);
            try {
                const response = await axios.get('http://localhost:8000/notes_operations/', {
                    headers: {
                        Authorization: `Token ${token}`,
                    },
                });
                setNotes(response.data);
                setLoading(false);
            } catch (error) {
                console.error('Failed to fetch notes:', error);
                setLoading(false);
            }
        };

        fetchNotes();
    }, []);

    const updateNote = async (id, updatedText) => {
        const token = localStorage.getItem('token');
        const updatedNote = {
            notes_text: updatedText,
            date: new Date().toLocaleDateString(),
        };

        try {
            await axios.put(`http://localhost:8000/pk_notes_operations/${id}`, updatedNote, {
                headers: {
                    Authorization: `Token ${token}`,
                },
            });
            setNotes(prevNotes => prevNotes.map(note => note.id === id ? { ...note, notes_text: updatedText } : note));
        } catch (error) {
            console.error('Failed to update note:', error);
        }
    };

    const deleteNote = async (id) => {
        const token = localStorage.getItem('token');
        try {
            await axios.delete(`http://localhost:8000/pk_notes_operations/${id}`, {
                headers: {
                    Authorization: `Token ${token}`,
                },
            });
            setNotes(prevNotes => prevNotes.filter(note => note.id !== id));
        } catch (error) {
            console.error('Failed to delete note:', error);
        }
    };

    if (loading) {
        return <div>Loading notes...</div>;
    }

    return (
        <div>
            {notes.map(note => (
                <Note
                    key={note.id}
                    id={note.id}
                    text={note.notes_text}
                    date={note.date}
                    handleDeleteNote={deleteNote}
                    handleUpdateNote={updateNote}
                />
            ))}
        </div>
    );
};

export default NotesManager;
