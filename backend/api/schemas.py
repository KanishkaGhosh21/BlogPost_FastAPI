from pydantic import BaseModel
from typing import Optional


class UserRequest(BaseModel):
    id: int
    name: str
    email: str
    password: str
    
    
class UserReponse(BaseModel):
    id: int
    name: str
    email: str


class NewPost(BaseModel):
    title: str
    content: str
    author: str

class UpdatePost(BaseModel):
    title: str | None = None
    content: str | None = None
    upvotes: int | None = None
    