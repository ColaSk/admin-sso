# -*- encoding: utf-8 -*-
"""
@File    :   user.py
@Time    :   2022/03/23 10:37:57
@Author  :   KX 
@Version :   1.0
@Contact :   ldu_sunkaixuan.163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
"""

# here put the import lib
from typing import Tuple, Union, Any

from apps.exceptions.exceptions import NotFound, Forbidden
from apps.extensions.tokens import create_token, verify_token
from apps.models.models import User
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import Depends
from functools import lru_cache

oauth2_scheme = OAuth2PasswordBearer("/api/v2/users/login")


class CurrUser(object):
    """当前用户
    func:
        登录
        权限
        验证
    """

    def __init__(self, model_obj: User):
        if model_obj is None:
            raise NotFound(detail="This user does not exist")
        self.obj = model_obj
            
    @property
    def model_obj(self) -> User:
        return self.obj
        
    @property
    def is_admin(self) -> bool:
        return self.obj.is_admin

    def to_dict(self, selects: tuple = None, excludes: tuple = None) -> dict:
        return self.model_obj.to_dict(selects, excludes)

    @classmethod
    async def parse_token(cls, token: str):
        """通过token 获取对象"""
        parse_token = verify_token(token)
        userdata = parse_token.get("data")
        user = await User.get_or_none(id=userdata.get('id'), is_del=False)
        return cls(user)
   
    @classmethod
    async def login(cls, username: str, password: str) -> str:
        """
        username -> phone
        password -> pwd
        """
        user = await User.get_or_none(phone=username, is_del=False)

        if not user:
            raise NotFound(detail=f"not found phone: {username} user")
        if not user.check_password(password):
            raise Forbidden(detail="password error")

        data = user.to_dict(("id", "created_time", "name", "phone"))
        token = create_token(data)

        return token
    
    def __getattr__(self, __name: str) -> Any:
        return getattr(self.model_obj, __name)


async def curr_user(token: str = Depends(oauth2_scheme)) -> CurrUser:
    """curr user"""
    return await CurrUser.parse_token(token)


async def admin_user(user: CurrUser = Depends(curr_user)) -> CurrUser:
    """admin user"""
    if not user.is_admin:
        raise Forbidden(detail="Insufficient permissions")
    return user
