  import { useEffect, useRef, useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [message, setMessage] = useState("");
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  const messagesEndRef = useRef(null);

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({
      behavior: "smooth",
    });
  }, [messages, loading]);

  const sendMessage = async () => {
    if (!message.trim() || loading) {
      return;
    }

    const userMessage = message.trim();

    setMessages((prev) => [
      ...prev,
      {
        role: "user",
        content: userMessage,
      },
    ]);

    setMessage("");
    setLoading(true);

    try {
      const result = await axios.post(
        "http://127.0.0.1:8000/chat",
        {
          message: userMessage,
        }
      );

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content: result.data.response,
        },
      ]);
    } catch (error) {
      console.error(error);

      setMessages((prev) => [
        ...prev,
        {
          role: "assistant",
          content:
            "Unable to connect to the AI backend. Please check whether the FastAPI server is running.",
        },
      ]);
    } finally {
      setLoading(false);
    }
  };

  const clearChat = () => {
    setMessages([]);
  };

  return (
    <div className="app">

      {/* Header */}
      <header className="header">
        <div>
          <h1 className="title">Personal AI Agent</h1>
          <p className="subtitle">
            Multi-Agent AI • Ollama + Mistral
          </p>
        </div>

        <button
          onClick={clearChat}
          className="clear-button"
        >
          Clear Chat
        </button>
      </header>

      {/* Chat Area */}
      <main className="chat-area">

        {messages.length === 0 && (
          <div className="welcome">

            <div className="logo">AI</div>

            <h2>How can I help you?</h2>

            <p>
              Ask a question, solve a calculation,
              or explore an AI topic.
            </p>

            <div className="examples">

              <button
                onClick={() =>
                  setMessage("What is Artificial Intelligence?")
                }
                className="example-button"
              >
                What is AI?
              </button>

              <button
                onClick={() =>
                  setMessage("What is RAG in AI?")
                }
                className="example-button"
              >
                What is RAG?
              </button>

              <button
                onClick={() =>
                  setMessage("What is 25 * 40?")
                }
                className="example-button"
              >
                Calculate 25 × 40
              </button>

            </div>
          </div>
        )}

        {/* Messages */}
        {messages.map((msg, index) => (
          <div
            key={index}
            className={
              msg.role === "user"
                ? "user-message-container"
                : "ai-message-container"
            }
          >

            <div
              className={
                msg.role === "user"
                  ? "user-avatar"
                  : "ai-avatar"
              }
            >
              {msg.role === "user" ? "You" : "AI"}
            </div>

            <div
              className={
                msg.role === "user"
                  ? "user-message"
                  : "ai-message"
              }
            >
              {msg.content}
            </div>

          </div>
        ))}

        {/* Loading */}
        {loading && (
          <div className="ai-message-container">

            <div className="ai-avatar">
              AI
            </div>

            <div className="ai-message">

              <div className="typing">
                <span></span>
                <span></span>
                <span></span>
              </div>

            </div>

          </div>
        )}

        <div ref={messagesEndRef} />

      </main>

      {/* Input */}
      <footer className="footer">

        <div className="input-wrapper">

          <input
            type="text"
            value={message}
            onChange={(e) => setMessage(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter") {
                sendMessage();
              }
            }}
            placeholder="Message your AI agent..."
            className="input"
            disabled={loading}
          />

          <button
            onClick={sendMessage}
            disabled={loading || !message.trim()}
            className="send-button"
          >
            Send
          </button>

        </div>

        <p className="footer-text">
          Personal AI Agent can use specialized agents
          for different tasks.
        </p>

      </footer>

    </div>
  );
}

export default App;