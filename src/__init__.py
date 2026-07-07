from fastapi import FastAPI
from src.books.book_router import router as book_router

app = FastAPI()
app.include_router(router=book_router)

@app.get("/")
async def get_root():
    return {
        "message" : "Hello World"
    }
