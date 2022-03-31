# -*- encoding: utf-8 -*-
'''
@File    :   init.py
@Time    :   2022/03/30 16:07:36
@Author  :   KX 
@Version :   1.0
@Contact :   ldu_sunkaixuan.163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib
import json
import os
from typing import List
from apps.models.models import User, Role, Permission
from config.setting import BASE_DIR
from apps.utils.utils import read_json

async def init_users(filepath: str):
    """初始化 用户表"""

    users: List[dict] = read_json(filepath)
    
    for u in users:
        user_model: User = User(
            id=u.get('id'),
            name=u.get('name', 'null'),
            email=u.get('email'),
            phone=u.get('phone'),
            pwd=u.get('password')
        )
        await user_model.save(force_update=True)

        role_ids = u.get('roles')

        if isinstance(role_ids, list):
            for i in role_ids:
                r = await Role.get_or_none(id=i)
                await user_model.roles.add(r)
        else:
            r = await Role.get_or_none(id=role_ids)
            await user_model.roles.add(r)


async def init_roles(filepath: str):
    """初始化 角色表"""

    roles: List[dict] = read_json(filepath)

    for r in roles:
        
        role_model, _ = await Role.update_or_create(
            id=r.get('id'),
            name=r.get('name', 'null'),
            desc=r.get('desc')
        )
        permission_ids = r.get('permissions')

        if isinstance(permission_ids, list):
            for i in permission_ids:
                p = await Permission.get_or_none(id=i)
                if not p:
                    raise Exception('Permission id: {i} not exist')
                await role_model.permissions.add(p)
        else:
            p = await Permission.get_or_none(id=i)
            if not p:
                raise Exception('Permission id: {i} not exist')
            await role_model.permissions.add(p)


async def init_permission(filepath: str):
    """初始化 权限表"""

    permissions = read_json(filepath)

    for p in permissions:
        await Permission.update_or_create(
            id=p.get('id',),
            name=p.get('name', 'null'),
            desc=p.get('desc')
        )


async def init():
    """权限数据初始化"""

    userpath = os.path.join(BASE_DIR, 'init/data/users.json')
    rolepath = os.path.join(BASE_DIR, 'init/data/roles.json')
    permissionpath = os.path.join(BASE_DIR, 'init/data/permission.json')

    await init_permission(permissionpath)
    await init_roles(rolepath)
    await init_users(userpath)


if __name__ == '__main__':

    pass