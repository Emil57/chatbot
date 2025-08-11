export default function ChatMessage({ sender, text }) {
  return (
    <div style={{ textAlign: sender === 'user' ? 'right' : 'left' }}>
      <b>{sender === 'user' ? 'You' : 'Bot'}:</b> {text}
    </div>
  );
}