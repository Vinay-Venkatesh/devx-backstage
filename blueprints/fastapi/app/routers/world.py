from fastapi import APIRouter

router = APIRouter(tags=["Demo"])

@router.get("/world")
def hello():
    return "World.."