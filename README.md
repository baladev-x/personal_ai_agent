# Personal AI Agent

A multi-agent AI assistant built using FastAPI, React, Ollama, and Mistral.

The system uses a Supervisor Agent to understand the user's request and route it to the appropriate specialized agent.

## Features

* Multi-agent AI architecture
* Supervisor Agent for task routing
* Calculator Agent for mathematical calculations
* Research Agent for technical, educational, and general questions
* Custom calculator tool
* FastAPI backend
* React frontend
* Ollama for local LLM inference
* Mistral language model
* Chat-based user interface
* Local AI processing without requiring an external LLM API key

## Architecture

User
|
v
Supervisor Agent
|
+-----------------------+
|                       |
v                       v
Calculator Agent    Research Agent
|                       |
v                       v
Calculator Tool         Mistral
|                       |
+-----------+-----------+
|
v
Final Response

## Tech Stack

### Frontend

* React
* Vite
* Axios
* CSS

### Backend

* Python
* FastAPI
* Pydantic
* Uvicorn

### AI

* Ollama
* Mistral

### Tools

* Python AST
* Custom Calculator Tool

## Project Structure

personal-ai-agent/
│
├── backend/
│   ├── agents/
│   │   ├── **init**.py
│   │   ├── supervisor.py
│   │   ├── calculator_agent.py
│   │   └── research_agent.py
│   │
│   ├── tools/
│   │   ├── **init**.py
│   │   └── calculator.py
│   │
│   ├── main.py
│   └── requirements.txt
│
├── frontend/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── main.jsx
│   │
│   ├── package.json
│   └── ...
│
├── .gitignore
└── README.md

## How It Works

1. The user sends a message through the React frontend.
2. React sends the request to the FastAPI backend.
3. FastAPI passes the message to the Supervisor Agent.
4. The Supervisor Agent determines which specialized agent should handle the request.
5. Mathematical requests are sent to the Calculator Agent.
6. The Calculator Agent extracts the mathematical expression and uses the Calculator Tool.
7. General, technical, and educational questions are sent to the Research Agent.
8. The Research Agent uses the Mistral model through Ollama.
9. The result is returned to the React frontend.

## Requirements

Before running the project, install:

* Python 3.10+
* Node.js
* Ollama
* Git

## Ollama Setup

Install Ollama and pull the Mistral model:

ollama pull mistral

Verify that the model is available:

ollama list

You can also test the model:

ollama run mistral

## Backend Setup

Open a terminal and navigate to the backend folder:

cd personal-ai-agent/backend

Create a virtual environment:

python -m venv venv

Activate the virtual environment on Windows:

venv\Scripts\activate

Install the required Python packages:

pip install -r requirements.txt

Start the FastAPI server:

uvicorn main:app --reload

The backend will run at:

http://127.0.0.1:8000

FastAPI Swagger documentation:

http://127.0.0.1:8000/docs

## Frontend Setup

Open another terminal and navigate to the frontend folder:

cd personal-ai-agent/frontend

Install dependencies:

npm install

If PowerShell blocks npm.ps1 on Windows, use:

npm.cmd install

Start the React development server:

npm.cmd run dev

The frontend will normally run at:

http://localhost:5173

## Example Questions

You can ask:

What is Artificial Intelligence?

What is RAG in AI?

Explain Machine Learning.

What is a neural network?

What is 25 * 40?

Calculate 100 / 5.

Explain Python functions.

## Example Workflow

For a mathematical question:

User:

What is 25 * 40?

Supervisor Agent
↓
Calculator Agent
↓
Calculator Tool
↓
1000

For an AI question:

User:

What is RAG in AI?

Supervisor Agent
↓
Research Agent
↓
Mistral
↓
Final Answer

## API

### POST /chat

Request:

{
"message": "What is 25 * 40?"
}

Response:

{
"response": "1000"
}

## Future Improvements

* Native Ollama tool calling
* More specialized agents
* Web research agent
* RAG agent
* Code generation agent
* File processing agent
* Memory system
* Conversation history
* Agent-to-agent communication
* LangChain integration
* LangGraph workflow
* Streaming responses
* Authentication
* Production deployment

## Learning Goals

This project was built to understand practical concepts in:

* Multi-agent systems
* LLM application development
* Agent routing
* Tool calling
* Local LLM inference
* FastAPI
* React
* AI system architecture

## License

This project is for educational and personal use.
