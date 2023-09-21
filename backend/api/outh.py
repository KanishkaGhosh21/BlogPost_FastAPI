from datetime import datetime,timedelta
from typing import Annotated
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from backend.database.models import Users
from backend.api.schemas import TokenData
from backend.database.utils import verify_password
from backend.config import settings
from jose import JWTError, jwt


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def authenticate_user(email, password, db):
    user=db.query(Users).filter(Users.email == email).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if not verify_password(password, user.password):
        raise HTTPException(status_code=400, detail="Incorrect password")
    return TokenData(userid=user.id)
    
def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


async def get_current_user(token: str=Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    
    return verify_access_token(token,credentials_exception)
    
    
def verify_access_token(token:str,credentials_exception:HTTPException):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("userid")
        if user_id is None:
            raise credentials_exception
        token_data = TokenData(userid=user_id)
    except JWTError:
        raise credentials_exception
    
    return token_data