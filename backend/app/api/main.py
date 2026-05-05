from fastapi import APIRouter

from .routes import home
from .routes import test

api_router = APIRouter()
api_router.include_router(home.router)
api_router.include_router(test.router)
