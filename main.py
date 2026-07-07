from fastapi import FastAPI
from data import books
from schemas.book_schema import Book
from typing import List

app = FastAPI()

@app.get("/")
async def get_root():
    return {
        "message" : "Hello World"
    }

@app.get("/books", response_model=List[Book],status_code=200)
async def get_books():
    return books

@app.post("/books", status_code=201)
async def get_book(book_data: Book) -> dict:
    new_book = book_data.model_dump()
    books.append(new_book)
    return new_book

@app.get("/book/{book_id}")
async def get_book(book_id: int) -> Book:
    pass

@app.patch("/book/{book_id}")
async def update_book(book_id: int):
    pass

@app.delete("/book/{book_id}")
async def delete_book(book_id: int):
    pass