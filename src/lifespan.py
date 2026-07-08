from contextlib import asynccontextmanager
from fastapi import FastAPI
from src.db.main import init_db

@asynccontextmanager
async def life_span(app: FastAPI):
    print(f"server is starting...")
    await init_db()
    yield 
    print(f"server has been stopped...")