from fastapi import APIRouter, Request, status
from fastapi.responses import RedirectResponse

from ui.templates import templates

router = APIRouter()

@router.get("/")
async def home(request: Request):
    return RedirectResponse(url="/todos", status_code=status.HTTP_302_FOUND)
    return templates.TemplateResponse("home.html", { "request": request })
