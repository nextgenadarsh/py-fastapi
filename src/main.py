# from .books.router import *

from fastapi import FastAPI
from .auth.router import router as auth_router
from .todos.router import router as todos_router
from .books.router import router as books_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(todos_router)
app.include_router(books_router)

