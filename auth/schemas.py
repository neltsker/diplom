from pydantic import EmailStr, BaseModel, UUID4
from typing import List, Optional



class User(BaseModel):
    id: Optional[int]
    firstName: str
    lastName: str
    email: str
    password:str


class UserCreate(User):
    firstName: str
    lastName: str
    email: str
    password:str
    
    


class UserUpdate(User):
    pass


class UserOut(BaseModel):
    id: int
    username: str
    avatar: str


class Token(BaseModel):
    id: int
    token: str


class TokenPayload(BaseModel):
    user_id: int = None