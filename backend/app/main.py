from fastapi import FastAPI

app = FastAPI(title="AI Reliability Platform")

@app.get("/health")
def health():
    return {"status": "ok"}
