from fastapi import APIRouter, FastAPI, Request
from fastapi.templating import Jinja2Templates

from ui.templates import templates

router = APIRouter(
    prefix="/auth"
)

@router.get("/register")
async def render_login(request: Request):
    return templates.TemplateResponse("auth/register.html", { "request": request })

@router.get("/login")
async def render_login(request: Request):
    return templates.TemplateResponse("auth/login.html", { "request": request })


