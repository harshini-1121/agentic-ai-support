from fastapi import FastAPI
from orchestrator import route_query

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Agentic AI system running 🚀"}

@app.post("/query")
def handle_query(user_query: str):
    response = route_query(user_query)
    return {"response": response}