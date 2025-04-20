from fastapi import APIRouter, Request

from ui.templates import templates

router = APIRouter(
    prefix="/todos"
)

@router.get("/")
async def home(request: Request):
    return templates.TemplateResponse("todos/todo-list.html", { "request": request })
