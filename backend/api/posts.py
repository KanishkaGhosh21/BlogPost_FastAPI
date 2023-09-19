from fastapi import APIRouter, Depends
from backend.database import models

from backend.database.db import SessionLocal,get_db
from . import schemas

from backend.database.utils import readAllPosts,readPostID,createPost,updatePost,deletePost


router=APIRouter(prefix="/api/posts",tags=["Posts"])

@router.get("/")
async def get_all_posts(db: SessionLocal = Depends(get_db)):
    posts=readAllPosts(db)
    return posts


@router.get("/{id}")
def get_post_with_id(id:int,db: SessionLocal = Depends(get_db)):
    post=readPostID(db,id)
    return post


@router.post("/")
def create_post(post:schemas.NewPost,db: SessionLocal = Depends(get_db)):
    newPost=createPost(db,post)
    return newPost


@router.put("/{id}")
def update_post(id:int,post:schemas.UpdatePost,db: SessionLocal = Depends(get_db)):
    updatedPost=updatePost(db,id,post)
    return updatedPost


@router.delete("/{id}")
def delete_post(id:int,db: SessionLocal = Depends(get_db)):
    return deletePost(db,id)    