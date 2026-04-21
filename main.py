from fastapi import FastAPI
from pydantic import BaseModel
from orchestrator import route_query
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {"message": "Agentic AI system running 🚀"}

class QueryRequest(BaseModel):
    user_query: str

@app.post("/query")
def handle_query(request: QueryRequest):
    response = route_query(request.user_query)
    return {"response": response}