from fastapi import FastAPI

from backend.database import models
from backend.database.db import engine
from backend.api import users
from backend.api import posts


app = FastAPI()


@app.get("/")
async def root():
    return {"server": "OK"}



app.include_router(users.router)
app.include_router(posts.router)
models.Base.metadata.create_all(bind=engine)