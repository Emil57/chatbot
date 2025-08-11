import { useState } from 'react';
import ChatMessage from '../components/ChatMessage';

export default function Chatbot() {
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState('');

  const sendMessage = async (e) => {
    e.preventDefault();
    if (!input.trim()) return;
    setMessages([...messages, { sender: 'user', text: input }]);
    const res = await fetch('http://localhost:5000/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ question: input }),
    });
    const data = await res.json();
    setMessages([...messages, { sender: 'user', text: input }, { sender: 'bot', text: data.answer }]);
    setInput('');
  };

  return (
    <div style={{ maxWidth: 600, margin: 'auto' }}>
      <ChatMessage sender="user" text="Hello!" />

      <h2>Audi Chatbot</h2>
      <div style={{ border: '1px solid #ccc', padding: 16, minHeight: 200 }}>
        {messages.map((msg, i) => (
          <div key={i} style={{ textAlign: msg.sender === 'user' ? 'right' : 'left' }}>
            <b>{msg.sender === 'user' ? 'You' : 'Bot'}:</b> {msg.text}
          </div>
        ))}
      </div>
      <form onSubmit={sendMessage} style={{ marginTop: 16 }}>
        <input
          value={input}
          onChange={e => setInput(e.target.value)}
          style={{ width: '80%', padding: 8 }}
          placeholder="Ask about Audi cars..."
        />
        <button type="submit" style={{ padding: 8 }}>Send</button>
      </form>
    </div>
  );
}