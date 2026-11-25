from fastapi import FastAPI
from app.core.config import settings
app = FastAPI(
    title="Expense Tracker API",
    version="0.1.0",
    debug=settings.debug
)


@app.get("/health")
async def health():
    return {"status": "ok"}