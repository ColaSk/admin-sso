from typing import List
from apps.extensions.response import BaseResponse
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    phone: str
    email: str
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
    phone: str
    email: str
    username: str
    password: str


class CreateResponse(BaseResponse):

    data: User


class UserInfoReResponse(BaseResponse):

    data: User
