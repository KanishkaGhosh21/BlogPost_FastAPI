from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.database import models
from backend.database.db import engine
from backend.api import users
from backend.api import posts
from backend.config import Settings


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"server": "OK"}

print(Settings)


app.include_router(users.router)
app.include_router(posts.router)
models.Base.metadata.create_all(bind=engine)