from fastapi import FastAPI
from src.lifespan import life_span
from src.books.book_router import router as book_router

version = "v1"

app = FastAPI(
    title="Bookly",
    description="A RestAPI for a book review web service",
    version=version,
    lifespan=life_span
)

app.include_router(router=book_router,prefix=f"/api/{version}/books")

@app.get("/")
async def get_root():
    return {
        "message" : "Hello World"
    }
