from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

from app.retriever import get_context
from app.llm import ask_llm


app = FastAPI(title="RAG Chatbot API")


# Serve frontend files
app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)


class QuestionRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return FileResponse("app/static/index.html")


@app.post("/ask")
def ask_question(request: QuestionRequest):

    context = get_context(request.question)

    # If no relevant document was found,
    # don't call OpenAI.
    if not context:
        return {
            "question": request.question,
            "answer": "I couldn't find that information in the document."
        }

    # Only call OpenAI when relevant context exists.
    answer = ask_llm(context, request.question)

    return {
        "question": request.question,
        "answer": answer
    }