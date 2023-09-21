from datetime import datetime
from pydantic import BaseModel, EmailStr


class UserRequest(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserReponse(BaseModel):
    id: int
    username: str
    email: EmailStr

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class NewPost(BaseModel):
    title: str
    content: str


class UpdatePost(BaseModel):
    title: str | None = None
    content: str | None = None
    upvotes: int | None = None

class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    upvotes: int
    author_id: int
    created_at : datetime
    updated_at : datetime

class DeletePostResponse(BaseModel):
    id: int
    status: str
    
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    userid: int
