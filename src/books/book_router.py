from fastapi import APIRouter, status, HTTPException, Depends
from typing import List
import uuid
from src.books.service import BookService
from sqlmodel.ext.asyncio.session import AsyncSession
from src.books.book_schema import Book, BookUpdate,BookCreate
from src.db.main import get_session

router = APIRouter()

book_service = BookService()

@router.get("/", response_model=List[Book],status_code=status.HTTP_200_OK)
async def get_books(session: AsyncSession = Depends(get_session)):
    books = await book_service.get_all_books(session)
    return books

@router.post("/", status_code=status.HTTP_201_CREATED,response_model=Book)
async def create_book(book_data: BookCreate,session: AsyncSession= Depends(get_session)) -> dict:
    new_book = await book_service.create_book(book_data,session)
    return new_book

@router.get("/{book_uid}")
async def get_book(book_uid: uuid.UUID,session: AsyncSession = Depends(get_session)) -> Book:
    book = await book_service.get_book(book_uid,session)   
    if book is not None:
        return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The book with {book_uid} wasn't found")

@router.patch("/{book_id}")
async def update_book(book_uid: uuid.UUID, book_update_data: BookUpdate,session: AsyncSession = Depends(get_session)):
    updated_book = await book_service.update_book(book_uid,book_update_data,session)
    if updated_book is not None:
        return updated_book

    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The book with {book_uid} wasn't found")

@router.delete("/{book_uid}",status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(book_uid: uuid.UUID,session: AsyncSession = Depends(get_session)):
    book_to_delete = await book_service.delete_book(book_uid,session)
    
    if book_to_delete:
        return None
    
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"The book with {book_uid} wasn't found")