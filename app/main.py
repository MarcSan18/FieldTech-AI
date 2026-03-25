from fastapi import FastAPI
from pydantic import BaseModel
from app.services.ai_service import responder

app = FastAPI()

class Pergunta(BaseModel):
    pergunta: str

@app.get("/")
def home():
    return {"status": "FieldTech AI rodando"}

@app.post("/chat")
def chat(data: Pergunta):
    resposta = responder(data.pergunta)
    return {"resposta": resposta}