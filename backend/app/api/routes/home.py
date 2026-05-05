from fastapi import APIRouter

from backend.app.core.logging import logger

router = APIRouter(prefix="/home", tags=["home"])


@router.get("/")
def home():
    return {"message": "Welcome to Bankify, YOUR all in one ERP system"}
