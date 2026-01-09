from fastapi import FastAPI
from pydantic import BaseModel
from datetime import datetime, timezone



import re

app = FastAPI(
    title="Text Analytics API",
    version="1.0.0"
)

class TextRequest(BaseModel):
    text: str

@app.get("/")
def root():
    return {
        "message": "Text Analytics API is running",
        "timestamp": datetime.now(timezone.utc)
    }


@app.get("/health")
def health():
    return {
        "status": "UP"
    }

@app.post("/analyze-text")#request
def analyze_text(data: TextRequest):
    text = data.text.strip()

    return {
        "words": len(text.split()),
        "characters": len(text),
        "sentences": len(re.findall(r"[.!?]", text)),
        "processed_at": datetime.now(timezone.utc)
    }
