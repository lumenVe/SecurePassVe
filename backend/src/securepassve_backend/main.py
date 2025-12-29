from fastapi import FastAPI

app = FastAPI(title="SecurePassVe API")

@app.get("/health")
def health():
    return {"status": "ok"}
