from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse
from datetime import datetime, timedelta, timezone
from utils.auth_utils import sign_in_auth_config
from utils.context import DEBUG

router = APIRouter()


@router.get("/sign-in")
async def sign_in(request: Request) -> RedirectResponse:
  if DEBUG < 2:
    config = sign_in_auth_config()
    url, state = config.authorization_url(access_type="offline", prompt="consent")

    response = RedirectResponse(url=url, status_code=302)
    expires = datetime.now(timezone.utc) + timedelta(minutes=5)
    response.set_cookie(
      key="state",
      value=state,
      expires=expires,
      path="/",
      secure=True,
      httponly=True,
      samesite="lax")
    return response
  else: return RedirectResponse("/home", status_code=302)


@router.get("/sign-out")
async def sign_out(request: Request) -> RedirectResponse:
  response = RedirectResponse(url="/", status_code=302)
  expires = datetime.now(timezone.utc) + timedelta(minutes=5)
  response.set_cookie(
    key="session_id",
    value="",
    expires=expires,
    path="/",
    secure=True,
    httponly=True,
    samesite="lax")
  return response
