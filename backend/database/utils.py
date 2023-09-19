from datetime import datetime
from fastapi import HTTPException
from backend.database import models


def readAllPosts(db):
    posts = db.query(models.Posts).all()
    if not posts:
        return {
            "status": "success", 
            "details": "No posts found."
        }
    return posts


def readPostID(db, id):
    post = db.query(models.Posts).filter(models.Posts.id == id).first()
    if not post:
        raise HTTPException(status_code=404, detail="No posts found")
    return post


def createPost(db, post):
    newPost=models.Posts(**post.dict())
    db.add(newPost)
    db.commit()
    db.refresh(newPost)
    return newPost

def updatePost(db, id, post):
    oldPost=db.query(models.Posts).filter(models.Posts.id == id).first()
    if not oldPost:
        raise HTTPException(status_code=404, detail="No posts found")
    newPost=oldPost
    isUpdated=False
    for var, value in vars(post).items():
        if value:
            setattr(newPost, var, value)
            isUpdated=True
    if isUpdated:
        newPost.updated_at=datetime.now()
        db.commit()
        db.refresh(newPost)
    return newPost


def deletePost(db, id):
    post=db.query(models.Posts).filter(models.Posts.id == id).first()
    if not post:
        raise HTTPException(status_code=404, detail="No posts found")
    db.delete(post)
    db.commit()
    return {
        "id": id,
        "status": "deleted"
    }
