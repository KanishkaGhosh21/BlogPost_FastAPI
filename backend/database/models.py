from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text
from .db import Base


class Posts(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    title = Column(String)
    content = Column(String)
    author = Column(String)
    upvotes = Column(Integer,server_default="0")
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text("now()"))
    updated_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default=text("now()"))
    
    
class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, nullable=False)
    username = Column(String,unique=True, nullable=False)
    email = Column(String,unique=True, nullable=False)
    password = Column(String, nullable=False)
