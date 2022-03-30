import os
from fastapi import APIRouter, Depends
from tortoise.transactions import atomic
from apps.extensions.route import LoggingRoute
from apps.models.models import User
from .depends import login as login_depend, curr_user_info, create_user
from .schemas import (
    UserCreate, NormalResponse, CreateResponse, UsersListResponse,
    SuccessResponse, UserInfoReResponse, LoginResponse
)
from .services import UserOperator
from init.init import init as datainit
from config.setting import BASE_DIR

router = APIRouter(route_class=LoggingRoute)


@router.post('/init',response_model=NormalResponse , status_code=200)
@atomic()
async def init():
    """模块用户权限表初始化
    # 初始化权限，角色，初级用户
    TODO: 后续迁移到指令集初始化
    """
    await datainit()
    return NormalResponse()


@router.post('/login',response_model=LoginResponse ,status_code=200)
async def login(login_info: dict = Depends(login_depend)):
    """登录
    args:
        login_info: dict {token: xxx, user: User}
    response:
        data: ex {token: xxx, user: {id: 0 ...}}
    """
    return LoginResponse(data=login_info)

@router.get('/user',response_model=UserInfoReResponse , status_code=200)
async def curr_user(user: User = Depends(curr_user_info)):
    """获取当前用户信息
    args:
        user User: 获取到的当前用户的对象
    """
    return UserInfoReResponse(data=user)

@router.post('/', response_model=CreateResponse, status_code=200)
async def add_user(user: User = Depends(create_user)):
    """添加用户
    args:
        user User: 添加后的用户对象
    """
    return CreateResponse(data=user)

@router.get('/', response_model=UsersListResponse, status_code=200)
async def get_users():
    """获取用户列表
    """
    users = await UserOperator.list()
    return UsersListResponse(data=users)