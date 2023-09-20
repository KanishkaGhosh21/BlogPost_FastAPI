from fastapi import APIRouter, Depends
from backend.api.outh import authenticate_user, create_access_token

from backend.api.schemas import UserLogin, UserReponse, UserRequest, Token
from backend.database.db import SessionLocal, get_db
from backend.database.utils import addNewUser, deleteUser, getAllUsers, getUsersWithId


router=APIRouter(prefix="/api/users",tags=["Users"])

@router.get("/",response_model=list[UserReponse])
def get_all_users(db:SessionLocal=Depends(get_db)):
    allUsers=getAllUsers(db)
    return allUsers

@router.get("/{id}",response_model=UserReponse)
def get_users_with_id(id:int,db:SessionLocal=Depends(get_db)):
    user=getUsersWithId(db,id)
    return user

@router.post("/",response_model=UserReponse)
def add_users(user:UserRequest, db: SessionLocal = Depends(get_db)):
    newUser=addNewUser(db,user)
    return newUser

@router.delete("/{id}")
def delete_users(id:int,db:SessionLocal=Depends(get_db)):
    return deleteUser(db,id)

@router.post("/login",response_model=Token)
def login(credentials:UserLogin, db:SessionLocal=Depends(get_db)):
    token_data=authenticate_user(credentials.email, credentials.password, db)
    token = create_access_token(token_data.dict())
    return {
        "access_token":token,
        "token_type":"bearer"
    }