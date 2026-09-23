from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from agents.supervisor import supervisor_agent


app = FastAPI(
    title="Multi-Agent Personal AI",
    description="Multi-agent AI system using Ollama and Mistral",
    version="1.0.0"
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    response: str


@app.get("/")
def home():

    return {
        "message": "Multi-Agent AI is running"
    }


@app.post("/chat", response_model=ChatResponse)
def chat_endpoint(request: ChatRequest):

    response = supervisor_agent(request.message)

    return {
        "response": response
    }