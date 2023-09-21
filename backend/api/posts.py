from fastapi import APIRouter, Depends
from backend.api.outh import get_current_user
from backend.database import models
from backend.api import schemas

from backend.database.db import SessionLocal,get_db
from . import schemas

from backend.database.utils import readAllPosts,readPostID,createPost,updatePost,deletePost


router=APIRouter(prefix="/api/posts",tags=["Posts"])


@router.get("/",response_model=list[schemas.PostResponse])
async def get_all_posts(db: SessionLocal = Depends(get_db)):
    posts=readAllPosts(db)
    return posts


@router.get("/{id}",response_model=schemas.PostResponse)
def get_post_with_id(id:int,db: SessionLocal = Depends(get_db)):
    post=readPostID(db,id)
    return post


@router.post("/",response_model=schemas.PostResponse)
def create_post(post:schemas.NewPost,db: SessionLocal = Depends(get_db), user_data: schemas.TokenData = Depends(get_current_user)):
    newPost=createPost(db,post,user_data.userid)
    return newPost


@router.put("/{id}",response_model=schemas.PostResponse)
def update_post(post_id:int,post:schemas.UpdatePost,db: SessionLocal = Depends(get_db), user_data: schemas.TokenData = Depends(get_current_user)):
    updatedPost=updatePost(db,post_id,post,user_data.userid)
    return updatedPost


@router.delete("/{id}",response_model=schemas.DeletePostResponse)
def delete_post(id:int,db: SessionLocal = Depends(get_db), username: schemas.TokenData = Depends(get_current_user)):
    return deletePost(db,id)    