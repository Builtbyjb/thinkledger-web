from fastapi import APIRouter, Request, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from middleware.authentication import auth_required
from utils.styles import BTN_STYLE_FULL
from utils.context import DEBUG


router = APIRouter(tags=["Integrations"])
templates = Jinja2Templates(directory="templates")


@router.get("/banking", status_code=status.HTTP_200_OK)
@auth_required(mode="strict")
async def banking(request: Request) -> HTMLResponse:
  username = request.state.username if DEBUG < 2 else "John Doe"
  return templates.TemplateResponse(
    request=request,
    name="auth/banking.html",
    context={"username": username, "btn_style_full": BTN_STYLE_FULL}
  )


@router.get("/google", status_code=status.HTTP_200_OK)
@auth_required(mode="strict")
async def google(request: Request) -> HTMLResponse:
  username = request.state.username if DEBUG < 2 else "John Doe"
  # TODO: Check for google api scopes for visually scope grant confirmation
  return templates.TemplateResponse(
    request=request,
    name="auth/google.html",
    context={"username": username, "btn_style_full": BTN_STYLE_FULL}
  )
