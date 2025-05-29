import os
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, JSONResponse
from routes import google, legal, support, user_auth, integrations, plaid, join_waitlist, index
from dotenv import load_dotenv
from database.postgres.postgres_db import create_db_and_tables
from middleware.rate_limiter import RateLimiter
from fastapi.templating import Jinja2Templates
from typing import Any
from contextlib import asynccontextmanager


# Load .env file
load_dotenv()


@asynccontextmanager
async def lifespan(app: FastAPI) -> Any:
  create_db_and_tables()
  yield

app = FastAPI(lifespan=lifespan, docs_url=None, redoc_url=None, openapi_url=None)

# Middleware
app.add_middleware(RateLimiter)

# Routes
app.include_router(index.router)
app.include_router(support.router)
app.include_router(legal.router)
app.include_router(user_auth.router)
app.include_router(google.router)
app.include_router(integrations.router)
app.include_router(plaid.router)
app.include_router(join_waitlist.router)

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")


# Health check
@app.get("/ping")
async def ping() -> JSONResponse:
  env_check = "Good" if os.getenv("ENV_CHECK") else "Bad"
  return JSONResponse(content={"env_check": env_check, "response": "pong"}, status_code=200)


# Handles page not found
@app.exception_handler(404)
async def not_found(request: Request, exc: Exception) -> HTMLResponse:
  return templates.TemplateResponse(request=request, name="not_found.html")
