from datetime import datetime
from fastapi import HTTPException
from backend.database import models
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


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

def addNewUser(db, user):
    hashedPassword=get_password_hash(user.password)
    user.password=hashedPassword
    newUser=models.Users(**user.dict())
    db.add(newUser)
    db.commit()
    db.refresh(newUser)
    return newUser

def deleteUser(db,id):
    user=db.query(models.Users).filter(models.Users.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="No users found")
    db.delete(user)
    db.commit()
    return {
        "id": id,
        "status": "deleted"
    }

def getAllUsers(db):
    users=db.query(models.Users).all()
    return users

def getUsersWithId(db,id):
    user=db.query(models.Users).filter(models.Users.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="No users found")
    return user

