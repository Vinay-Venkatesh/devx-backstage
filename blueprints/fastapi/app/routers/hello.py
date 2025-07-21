from fastapi import APIRouter

router = APIRouter(tags=["Demo"])

@router.get("/hello")
def hello():
    return "Hello.."