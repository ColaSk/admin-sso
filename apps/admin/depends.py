# -*- encoding: utf-8 -*-
'''
@File    :   depends.py
@Time    :   2022/03/23 22:17:12
@Author  :   KX 
@Version :   1.0
@Contact :   ldu_sunkaixuan.163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
from typing import Dict, List, Tuple, Union
from .schemas import UserCreate, UserLogin
from apps.models.models import User
from apps.modules.user import CurrUser
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends

oauth2_scheme = OAuth2PasswordBearer('/api/v2/users/login')

async def login(
    user: OAuth2PasswordRequestForm = Depends()) -> Dict[str, Union[str, User]]:
    token, userobj = await CurrUser.login(user.username, user.password)
    return {
        'token': token, 
        'user': userobj
    }


async def curr_user(
    token: str = Depends(oauth2_scheme)) -> CurrUser:
    return await CurrUser.get_obj_by_token(token)


async def curr_user_info(
    user: CurrUser = Depends(curr_user)) -> User:
    return user.obj


async def create_user(
    body: UserCreate, 
    curr_user: CurrUser = Depends(curr_user))-> User:

    user = User(name=body.username)
    user.password = body.password # 密码哈希
    await user.save()
    return user
