# from .books.router import *

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from ui.home.router import router as ui_home_router
from ui.auth.router import router as ui_auth_router
from ui.todos.router import router as ui_todos_router

from api.auth.router import router as auth_router
from api.todos.router import router as todos_router
from api.books.router import router as books_router

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/health")
def health_check():
    return { 'status': 'Healthy' }

app.include_router(ui_home_router)
app.include_router(ui_auth_router)
app.include_router(ui_todos_router)
app.include_router(auth_router)
app.include_router(todos_router)
app.include_router(books_router)

