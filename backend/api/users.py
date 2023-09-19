from fastapi import APIRouter


router=APIRouter(prefix="/api/users",tags=["Users"])

@router.get("/")
def get_users():
    return {"users":"all users"}