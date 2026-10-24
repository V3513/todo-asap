from fastapi import FastAPI
from sqlalchemy import text
from app.core.database import engine

app = FastAPI(title="todo-asap API")

@app.get("/")
def root():
    return {"message": "todo-asap API"}

@app.get("/health/db")
async def database_health():
    async with engine.connect() as connection:
        result = await connection.execute(text("SELECT 1"))
        return {"database": "connected", "result": result.scalar_one()}
