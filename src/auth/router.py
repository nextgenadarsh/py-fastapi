# auth main router with all the endpoints

from datetime import datetime, timedelta, timezone
from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import jwt, JWTError

from .models import Users
from .schemas import UserRequest, Token
from ..database import db_dependency

SECRET_KEY = "d0b75e04a1e07a02c7f131fd7f37bdd98dffd3fa313cbd985454bedcf5d611b"
ALGORITHM = 'HS256'

router = APIRouter(
    prefix='/auth',
    tags=['auth']
)
bcrypt_context = CryptContext(schemes=['bcrypt'], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl='auth/token')

@router.post("/users", status_code=status.HTTP_201_CREATED)
async def create_user(user_request: UserRequest,
                      db: db_dependency):
    user: Users = Users (
        email = user_request.email,
        user_name = user_request.username,
        first_name = user_request.first_name,
        last_name = user_request.last_name,
        roles = user_request.roles,
        hashed_password =  bcrypt_context.hash(user_request.password),
        is_active = True   
    )
    print("[",user_request.password,"]", user.hashed_password)
    db.add(user)
    db.commit()

def authenticate_user(username: str, password: str, db: Session):
    user = db.query(Users).filter(Users.user_name == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False
    return user

def create_access_token(user_name: str, user_id: int, expires_delta: timedelta):
    encode = { 'sub': user_name, 'id': user_id }
    expires = datetime.now(timezone.utc) + expires_delta
    encode.update({'exp': expires})
    return jwt.encode(encode, SECRET_KEY, algorithm=ALGORITHM)

@router.post("/user")
async def get_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get('sub')
        user_id: int = payload.get('id')
        if username is None or user_id is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user')
        return {'username': username, 'id': user_id}
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user')

@router.post("/token", response_model=Token)
async def get_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                    db: db_dependency):
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Could not validate user')
    token = create_access_token(user.user_name, user.id, timedelta(minutes=30))
    return Token(access_token=token, token_type='bearer')

@router.post("/login")
async def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
                db: db_dependency):
    user = db.query(Users).filter(Users.user_name == form_data.username).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    if not authenticate_user(form_data.username, form_data.password, db):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return "Successfully authenticated"    
    
