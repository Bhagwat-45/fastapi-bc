from fastapi import FastAPI
from src.books.book_router import router as book_router

version = "v1"

app = FastAPI(
    title="Bookly",
    description="A RestAPI for a book review web service",
    version=version
)

app.include_router(router=book_router,prefix=f"/api/{version}/books")

@app.get("/")
async def get_root():
    return {
        "message" : "Hello World"
    }
