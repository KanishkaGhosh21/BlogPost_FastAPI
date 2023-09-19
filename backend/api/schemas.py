from pydantic import BaseModel, EmailStr


class UserRequest(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserReponse(BaseModel):
    id: int
    username: str
    email: EmailStr


class NewPost(BaseModel):
    title: str
    content: str
    author: str


class UpdatePost(BaseModel):
    title: str | None = None
    content: str | None = None
    upvotes: int | None = None
