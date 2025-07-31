import React, { useState } from 'react';
import './App.css';

const messages = [
  "You're doing amazing!",
  "Keep going, sweet",
  "You light up the world ✨",
  "You're stronger than you think 💪",
  "Today is full of possibilities 🌈",
];

function App() {
  const [name, setName] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (name.trim()) {
      const randomMsg = messages[Math.floor(Math.random() * messages.length)];
      setMessage(`${randomMsg} ${name}!`);
    }
  };

  return (
    <div className="container">
      <div className="background">
        <div className="blob blob1" />
        <div className="blob blob2" />
        <div className="blob blob3" />
      </div>

      <div className="card">
        <h2>Hello there 👋</h2>
        <form onSubmit={handleSubmit}>
          <input
            type="text"
            placeholder="What's your name?"
            value={name}
            onChange={(e) => setName(e.target.value)}
          />
          <button type="submit">Get a boost!</button>
        </form>
        {message && <p className="message">{message}</p>}
      </div>
    </div>
  );
}

export default App;
