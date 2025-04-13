from fastapi import Body, FastAPI, HTTPException, Path, Query, status
from starlette import status
from .schemas import BookRequest
from .models import Book

app = FastAPI()

BOOKS = [
    Book(101, "Book 1", "science"),
    Book(102, "Book 2", "Math"),
    Book(103, "Book 3", "Physics"),
    Book(104, "Book 4", "Science"),
    Book(105, "Book 5", "Math")
]

@app.post("/books", status_code = status.HTTP_201_CREATED)
async def create_book(book: BookRequest):
    book_to_create = Book(**book.model_dump())
    book_to_create.id = 1 if BOOKS.count == 0 else BOOKS[-1].id + 1
    BOOKS.append(book_to_create)
    return book_to_create

@app.put("/books/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_book(id: int, book: BookRequest):
    foundBook = next((b for b in BOOKS if b.id == id), None)
    if foundBook != None:
        foundBook.title = book.title
        foundBook.category = book.category
        return foundBook
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

@app.get("/books", status_code=status.HTTP_200_OK)
async def get_books(category: str = Query(default=None, min_length=3)):
    return [book for book in BOOKS if not category or book.category.casefold() == category.casefold()]

@app.get("/books/{id}")
async def get_book(id: int = Path(gt=0, lt=900)):
    book = next((book for book in BOOKS if book.id == id), None)
    if book != None:
        return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

@app.delete("/books/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_book(id: int):
    foundBook = next((b for b in BOOKS if b.id == id), None)
    if foundBook != None:
        BOOKS.remove(foundBook)
