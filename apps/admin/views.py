from typing import Any, Optional
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from pydantic import BaseModel
from apps.extensions.route import LoggingRoute
from apps.modules.user import CurrUser

from .schemas import (
    UserCreate, NormalResponse, CreateResponse, UsersListResponse,
    SuccessResponse
)
from .services import UserOperator

router = APIRouter(route_class=LoggingRoute)


@router.post('/login',response_model=SuccessResponse ,status_code=200)
async def login(form: OAuth2PasswordRequestForm = Depends()):
    """登录"""
    token, userdata = await UserOperator.login(form)
    result = {'token': token, 'user': userdata}
    return SuccessResponse(data=result)

@router.get('/user',response_model=SuccessResponse , status_code=200)
async def curr_user(user: CurrUser = Depends(UserOperator.curr_user)):
    return SuccessResponse(data=user.to_dict(('id', 'name', 'created_time')))

@router.post('/', response_model=CreateResponse, status_code=200)
async def add_user(body: UserCreate):
    """添加用户"""
    user = await UserOperator.create(body)
    return CreateResponse(data=user)

@router.get('/', response_model=UsersListResponse, status_code=200)
async def get_users():
    """获取用户列表"""
    users = await UserOperator.list()
    return UsersListResponse(data=users)