from tortoise import fields
from typing import Any
from .mixin import (ModelBase, DelModelBase, TimeModelBase, 
                    AdjTreeModelBase, ExtraInfoModelBase, 
                    Many2ManyModelBase, ModelMixin)
from apps.utils.passlib_context import hash, verify


class User(ModelBase, 
           DelModelBase, 
           TimeModelBase,
           ExtraInfoModelBase,
           ModelMixin):

    name = fields.CharField(max_length=255, description="name")
    pwd = fields.CharField(max_length=255, description="password hash")
    phone = fields.CharField(max_length=255, unique=True, description="phone")

    is_admin = fields.BooleanField(
        default=False, description="Background administrator, only for background module")
        
    email = fields.CharField(max_length=255, description="email")

    def __init__(self, **kwargs: Any) -> None:
        kwargs["pwd"] = hash(kwargs["pwd"])  # 将 password 转为 hash
        super().__init__(**kwargs)

    class Meta:
        table = "users"
        table_description = "用户表"

    @property
    def password(self):
        return self.pwd

    @password.setter
    def password(self, value):
        self.pwd = hash(value)

    def check_password(self, password: str) -> bool:
        return verify(password, self.password)


class UserAndRole(ModelBase, Many2ManyModelBase, ModelMixin):

    user_id = fields.IntField(index=True, description="用户id")
    role_id = fields.IntField(index=True, description="角色id")

    class Meta:
        table = "user_and_role"
        table_description = "用户角色中间表"


class Role(ModelBase, 
           DelModelBase, 
           TimeModelBase,
           ExtraInfoModelBase, 
           ModelMixin):

    name = fields.CharField(max_length=255, description="name")
    description = fields.TextField(description="desc")

    class Meta:
        table = "roles"
        table_description = "角色表"


class RoleAndMenuPermission(ModelBase, Many2ManyModelBase, ModelMixin):
    
    role_id = fields.IntField(index=True, description="角色id")
    menu_id = fields.IntField(index=True, description="菜单id")

    class Meta:
        table = "role_and_menu"
        table_description = "角色与菜单权限中间表"


class MenuPermission(ModelBase, 
                     DelModelBase, 
                     TimeModelBase,
                     AdjTreeModelBase,
                     ExtraInfoModelBase,
                     ModelMixin):

    name = fields.CharField(max_length=255, description="name")
    description = fields.TextField(description="desc")

    class Meta:
        table = "menu_permission"
        table_description = "菜单权限表"


class APIPermission(ModelBase, 
                    DelModelBase, 
                    TimeModelBase,
                    ExtraInfoModelBase,
                    ModelMixin):

    name = fields.CharField(max_length=255, description="name")
    menu_id = fields.IntField(description="菜单id")
    method = fields.CharField(max_length=20, description="方法")
    route = fields.CharField(max_length=255, description="路由")
    description = fields.TextField(description="desc")

    class Meta:
        table = "api_permission"
        table_description = "api权限"
