from fastapi import FastAPI
from sqlalchemy import text

from app.auth.router import router as auth_router
from app.db.database import engine


app = FastAPI(
    title="Spendora API",
    version="0.1.0",
)

app.include_router(auth_router)


@app.get("/api/health")
def health():
    return {
        "status": "ok",
        "service": "spendora-api",
    }


@app.get("/api/health/db")
def database_health():
    with engine.connect() as connection:
        connection.execute(text("SELECT 1"))

    return {
        "status": "ok",
        "database": "connected",
    }
