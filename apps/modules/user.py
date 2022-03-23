# -*- encoding: utf-8 -*-
'''
@File    :   user.py
@Time    :   2022/03/23 10:37:57
@Author  :   KX 
@Version :   1.0
@Contact :   ldu_sunkaixuan.163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
from typing import Tuple
from apps.extensions.tokens import verify_token, create_token
from apps.exceptions.exceptions import NotFound
from apps.models.models import User

class CurrUser(object):
    """当前用户
    func:
        登录
        权限
        验证
    """

    def __init__(self, id: int, name: str, userobj: User ,**kwargs):

        self.id = id
        self.name = name
        self.obj = userobj
    
    def to_dict(self, selects: tuple = None, excludes: tuple = None) -> dict:
        return self.obj.to_dict(selects, excludes)
    
    @classmethod
    async def get_obj_by_token(cls, token: str):
        """通过token获取当前用户对象"""
        
        tokeninfo = verify_token(token)
        userdata = tokeninfo.get('data')

        user = await User.get_or_none(id=userdata.get('id'), is_del=False)

        if user:
            return cls(user.id, user.name, user)
        else:
            raise NotFound(detail=f"not find id: {userdata.get('id')} user")
    
    @classmethod
    async def login(cls, username: str, password: str)-> Tuple[str, User]:

        user = await User.get_or_none(name=username, is_del=False)

        if not user:
            raise NotFound(msg=f' not found username: {username} user')

        if not user.check_password(password):
            raise Exception('password error')

        userdata = user.to_dict(('id', 'created_time', 'name'))

        token = create_token(userdata)

        return token, user