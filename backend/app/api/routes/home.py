from fastapi import APIRouter

router = APIRouter(prefix="/home", tags=["home"])


@router.get("/")
def home():
    return {"message": "Welcome to Bankify, YOUR all in one ERP system"}
