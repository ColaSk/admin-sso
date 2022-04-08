import os
from apps.exceptions.status import status

from apps.extensions.response import NormalResponse
from apps.extensions.route import LoggingRoute
from apps.models.models import User
from apps.modules.user import CurrUser, admin_user
from apps.modules.user import curr_user as curruser_dep
from fastapi import APIRouter, Depends
from init.init import init as datainit
from tortoise.transactions import atomic

from .depends import create_user, delete_user_dep, update_user_dep
from .depends import login as login_depend
from .schemas import (CreateResponse, LoginResponse,
                      UserInfoReResponse, UsersListResponse)
from .services import UserOperator

router = APIRouter(route_class=LoggingRoute)


@router.post("/init", response_model=NormalResponse, status_code=200)
@atomic()
async def init():
    """模块用户权限表初始化
    # 初始化权限，角色，初级用户
    TODO: 后续迁移到指令集初始化
    """
    await datainit()
    return NormalResponse()


@router.post("/login", response_model=LoginResponse, status_code=200)
async def login(login_info: dict = Depends(login_depend)):
    """登录
    args:
        login_info: dict {token: xxx, user: User}
    response:
        data: ex {token: xxx, user: {id: 0 ...}}
    """
    return LoginResponse(data=login_info)


@router.get("/user", response_model=UserInfoReResponse, status_code=200)
async def curr_user(user: CurrUser = Depends(curruser_dep)):
    """获取当前用户信息
    args:
        user User: 获取到的当前用户的对象
    """
    return UserInfoReResponse(data=user.model_obj)


@router.post("/", response_model=CreateResponse, status_code=200)
async def add_user(user: User = Depends(create_user)):
    """注册用户
    args:
        user User: 添加后的用户对象
    """
    return CreateResponse(data=user)


@router.delete('/{id}', response_model=NormalResponse, status_code=status.HTTP_200_OK)
async def del_user(success: bool = Depends(delete_user_dep)) -> NormalResponse:
    """删除用户
    """
    return NormalResponse()


@router.post('/{id}', response_model=UserInfoReResponse, status_code=status.HTTP_200_OK)
async def update_user(user_: User = Depends(update_user_dep)):
    return UserInfoReResponse(data=user_)


@router.get("/", response_model=UsersListResponse, status_code=200)
async def get_users(admin: CurrUser = Depends(admin_user)) -> UsersListResponse:
    """获取用户列表"""
    users = await UserOperator.list()
    return UsersListResponse(data=users)
