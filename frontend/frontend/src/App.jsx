import "./App.css";
import { useState } from "react";

function App() {
  const [question, setQuestion] = useState("");
  const [answer, setAnswer] = useState("");
  const [sources, setSources] = useState([]);
  const [loading, setLoading] = useState(false);

  const handleAsk = async () => {
    if (!question.trim()) return;

    setLoading(true);
    setAnswer("");
    setSources([]);

    try {
      const response = await fetch("http://127.0.0.1:5000/ask", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          question: question,
        }),
      });

      if (!response.ok) {
        throw new Error(`HTTP Error: ${response.status}`);
      }

      const data = await response.json();

      setAnswer(data.answer);
      setSources(data.sources || []);
    } catch (error) {
      console.error(error);
      setAnswer("Failed to connect to backend.");
    }

    setLoading(false);
  };

  return (
    <div className="app">
      <div className="container">
        <header className="header">
          <h1>⚡ DIR Compliance Agent</h1>
          <p>Search California DIR regulations using AI</p>
        </header>

        <div className="search-section">
          <input
            className="question-input"
            placeholder="Ask a compliance question..."
            value={question}
            onChange={(e) => setQuestion(e.target.value)}
            onKeyDown={(e) => {
              if (e.key === "Enter") {
                handleAsk();
              }
            }}
          />

          <button
            className="ask-btn"
            onClick={handleAsk}
            disabled={loading}
          >
            {loading ? "Loading..." : "Ask"}
          </button>
        </div>

        <div className="answer-card">
          <div className="answer-header">
            AI Response
          </div>

          <div className="answer-content">
            {answer ||
              "Responses from the compliance assistant will appear here."}
          </div>

          {sources.length > 0 && (
            <>
              <div className="sources-title">
                Sources
              </div>

              <div className="sources">
                {sources.map((source, index) => (
                  <a
                    key={index}
                    href={source}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="source-pill"
                  >
                    📄 DIR Source {index + 1}
                  </a>
                ))}
              </div>
            </>
          )}
        </div>
      </div>
    </div>
  );
}

export default App;