import React, { useState } from "react";

function Chatbot() {
  const [input, setInput] = useState("");
  const [messages, setMessages] = useState([]);

  const sendMessage = async () => {
    const response = await fetch("/chat", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ message: input }),
    });
    const data = await response.json();
    setMessages([...messages, { sender: "User", text: input }, { sender: "Bot", text: data.reply }]);
    setInput("");
  };

  return (
    <div>
      {messages.map((msg, idx) => (
        <p key={idx}><strong>{msg.sender}:</strong> {msg.text}</p>
      ))}
      <input value={input} onChange={(e) => setInput(e.target.value)} />
      <button onClick={sendMessage}>Send</button>
    </div>
  );
}

export default Chatbot;
