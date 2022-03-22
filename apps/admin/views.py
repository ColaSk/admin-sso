from typing import Any, Optional
from fastapi import APIRouter, Depends
from pydantic import BaseModel
from apps.extensions.route import LoggingRoute
from .schemas import UserCreate, NormalResponse, CreateResponse, UsersListResponse
from .services import UserOperator

router = APIRouter(route_class=LoggingRoute)


@router.post('/login',response_model=NormalResponse ,status_code=200)
def login():
    """登录 TODO: 待实现"""
    return NormalResponse()

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