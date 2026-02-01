from fastapi import FastAPI, Query
from pydantic import BaseModel
import re

app = FastAPI(title="Sentence Counter", version="v1")

class Health(BaseModel):
    ok: bool

class SentenceCountResponse(BaseModel):
    input: str
    sentence_count: int

@app.get("/health", response_model=Health)
def health():
    return {"ok": True}

@app.get("/v1/sentence-count", response_model=SentenceCountResponse)
def sentence_count(text: str = Query(..., description="Text to count sentences for")):
    # Simple rule: count ., !, ? followed by space or end of string
    sentences = re.findall(r"[.!?]+(?:\s|$)", text)
    return {"input": text, "sentence_count": len(sentences)}
