from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from datetime import datetime
from app.db.mysql import get_connection
from app.rag.qa import get_answer

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for development only
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class QueryRequest(BaseModel):
    query: str


@app.get("/")
def home():
    return {"message": "AI Logistics Assistant Running"}


@app.post("/query")
def query(request: QueryRequest):
    print("API HIT")

    # 1. Get answer from RAG
    response_text = get_answer(request.query)

    # 2. Save to DB
    try:
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(
    "INSERT INTO queries (query, response) VALUES (%s, %s)",
    (request.query, response_text)
    )

        conn.commit()
        cursor.close()
        conn.close()

    except Exception as e:
        print("DB Error:", e)

    # 3. Return response
    return {
        "query": request.query,
        "response": response_text
    }