from typing import Any, List
from datetime import datetime
from apps.extensions.response import BaseResponse, NormalResponse,SuccessResponse
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    created_time: str
    updated_time: str

    class Config:
        orm_mode = True


class UsersListResponse(BaseResponse):
    data: List[User]


class UserLogin(BaseModel):
    username: str
    password: str


class loginResInfo(BaseModel):
    token: str
    user: User

class LoginResponse(BaseResponse):
    data: loginResInfo


class UserCreate(BaseModel):
    username: str
    password: str

class CreateResponse(BaseResponse):

    data: User

class UserInfoReResponse(BaseResponse):

    data: User



