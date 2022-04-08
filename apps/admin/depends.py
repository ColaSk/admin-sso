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
from typing import Dict, Union

from apps.models.models import User
from apps.modules.user import CurrUser, curr_user
from apps.exceptions.exceptions import Forbidden, NotFound
from fastapi import Depends, Path
from fastapi.security import OAuth2PasswordRequestForm

from .schemas import UserCreate


async def login(
    user: OAuth2PasswordRequestForm = Depends(),
) -> Dict[str, Union[str, User]]:

    token = await CurrUser.login(user.username, user.password)
    return {"token": token}


async def create_user(body: UserCreate) -> User:
    return await User.create(
        phone=body.phone, email=body.email, name=body.username, pwd=body.password)


async def delete_user_dep(
    id: int = Path(...),
    curr_user: CurrUser = Depends(curr_user)
) -> bool:

    if id == curr_user.id:
        await curr_user.update_from_dict({"is_del": True}).save()
    elif curr_user.is_admin:
        user = await User.get_or_none(id=id, is_del=False)
        if user:
            await user.update_from_dict({"is_del": True}).save()
        else:
            raise NotFound(detail=f"user: {id} not existent")
    else:
        raise Forbidden(detail="No operation permission")
    return True
