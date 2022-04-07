# -*- encoding: utf-8 -*-
"""
@File    :   depends.py
@Time    :   2022/03/23 22:17:12
@Author  :   KX 
@Version :   1.0
@Contact :   ldu_sunkaixuan.163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
"""

# here put the import lib
from typing import Dict, List, Tuple, Union

from apps.models.models import User
from apps.modules.user import CurrUser
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from .schemas import UserCreate, UserLogin


async def login(
    user: OAuth2PasswordRequestForm = Depends(),
) -> Dict[str, Union[str, User]]:

    token = await CurrUser.login(user.username, user.password)
    return {"token": token}


async def create_user(body: UserCreate) -> User:

    user = User(
        phone=body.phone, email=body.email, name=body.username, pwd=body.password
    )
    await user.save()

    return user
