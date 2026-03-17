from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from rag.db_retriever import DBRetriever
from rag.vector_retriever import VectorRetriever
from rag.serpapi_retriever import SerpAPIRetriever
from rag.router import QueryRouter
from rag.merger import merge_context
from llm.model import generate_answer

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Sample vector docs
docs = [
    "Hospital admission requires ID proof",
    "Emergency cases are prioritized",
    "ICU has restricted access"
]

router = QueryRouter()
db = DBRetriever()
vector = VectorRetriever(docs)
web = SerpAPIRetriever()

class QueryRequest(BaseModel):
    query: str

@app.get("/")
def home():
    return {"message": "Medical Multi-RAG running"}

@app.post("/ask")
def ask(req: QueryRequest):
    route = router.route(req.query)

    if route == "db":
        data = db.query(req.query)
    elif route == "vector":
        data = vector.query(req.query)
    else:
        data = web.query(req.query)

    context = merge_context(data)
    answer = generate_answer(context, req.query)

    return {
    "query": req.query,
    "route": route,
    "context": context,
    "answer": answer
}