from typing import Any, List
from datetime import datetime
from apps.extensions.response import BaseResponse, NormalResponse
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name: str
    created: datetime
    updated: datetime


class UsersListResponse(BaseResponse):
    data: List[User]


class UserCreate(BaseModel):
    username: str
    password: str

class CreateResponse(BaseResponse):

    data: User



