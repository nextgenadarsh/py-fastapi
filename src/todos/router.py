from typing import Annotated
from fastapi import Body, FastAPI, APIRouter, Depends, HTTPException, Path, Query, status
from starlette import status
from sqlalchemy.orm import Session

from .schemas import TodoRequest
from .models import *
from ..auth.router import get_user
from ..database import db_dependency

router = APIRouter()

user_dependency = Annotated[dict, Depends(get_user)]

@router.get("/todos")
async def get_todos(db: db_dependency):
    return db.query(Todos).all()

@router.get("/todos/{id}", status_code=status.HTTP_200_OK)
async def get_todo(db: db_dependency, id: int = Path(gt=0)):
    record = db.query(Todos).get(id)
    if record is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return record

@router.post("/todos", status_code=status.HTTP_201_CREATED)
async def create_todo(user: user_dependency,
                      db: db_dependency, 
                      todo: TodoRequest):
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    todo_model = Todos(**todo.model_dump(), owner_id=user.get(id))
    todo_model.owner_id = 1
    db.add(todo_model)
    db.commit()

@router.put("/todos/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_todos(db: db_dependency, 
                       todo: TodoRequest,
                       id: int = Path(gt=0)):
    record: Todos = db.query(Todos).filter(Todos.id == id).first()
    if record is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    record.title = todo.title
    record.description = todo.description
    record.priority = todo.priority
    record.complete = todo.complete
    db.add(record)
    db.commit()

@router.delete("/todos/{id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_todo(db: db_dependency, id: int = Path(gt=0)):
    todo = db.query(Todos).get(id)
    if todo is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    # record: Todos = db.query(Todos).filter(Todos.id == id).delete()
    
    db.delete(todo)
    db.commit()
