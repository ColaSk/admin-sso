import typing as t
from apps.models.models import Role
from apps.exceptions.exceptions import NotFound


class RoleService(object):

    async def create(self, request: dict) -> Role:
        """创建角色"""
        role = await Role.create(**request)
        return role

    async def update(self, id: int, request: dict) -> Role:
        """更新角色"""

        role: t.Optional[Role] = Role.get_or_none(id=id, is_del=False)
        if not role:
            raise NotFound(detail=f"id: {id} - 此角色不存在")
        
        role.update_from_dict(request)

        return role

    async def delete(self, id: int) -> bool:
        """删除角色(逻辑删除)"""
        
        role: t.Optional[Role] = Role.get_or_none(id=id, is_del=False)
        if not role:
            raise NotFound(detail=f"id: {id} - 此角色不存在")
        
        role.update_from_dict(dict(is_del=True))

        return True

    async def select(self, request: t.Optional[dict]) -> t.List[Role]:
        """获取角色列表"""

        # TODO: 后续增加角色筛选功能
        if request:
            return []
        roles = Role.all()
        return roles

    async def update_menu_permission(self, menu_tree: t.Dict[t.List[dict]]):
        """更新角色菜单权限"""
        pass

    async def update_api_permission(self, type: str, request: dict):
        """ 更新角色api权限"""
        pass

    async def add_api_permission(self):
        """添加角色api权限"""
        pass

    async def delete_api_permission(self):
        """删除角色api权限"""
        pass
    