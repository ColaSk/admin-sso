from tortoise import fields
from typing import Any
from .mixin import ModelBase, DelModelBase, TimeModelBase, ModelMixin
from apps.utils.passlib_context import hash, verify


class User(ModelBase, DelModelBase, TimeModelBase, ModelMixin):

    name = fields.CharField(max_length=255, null=False, description="name")
    pwd = fields.CharField(max_length=255, null=False, description="password hash")
    phone = fields.CharField(
        max_length=255, null=False, unique=True, description="phone")

    is_admin = fields.BooleanField(
        default=False, description="Background administrator, only for background module")
        
    email = fields.CharField(max_length=255, description="email")
    roles = fields.ManyToManyField(
        "models.Role",
        related_name="users",
        through="user_role",
        n_delete=fields.SET_NULL,
    )

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


class Role(ModelBase, DelModelBase, TimeModelBase, ModelMixin):

    name = fields.CharField(max_length=255, null=False, description="name")
    desc = fields.TextField(description="desc")
    permissions = fields.ManyToManyField(
        "models.Permission",
        related_name="roles",
        through="role_permission",
        on_delete=fields.SET_NULL,
    )

    class Meta:
        table = "roles"
        table_description = "角色表"


class Permission(ModelBase, DelModelBase, TimeModelBase, ModelMixin):

    name = fields.CharField(max_length=255, null=False, description="name")
    desc = fields.TextField(description="desc")

    class Meta:
        table = "permission"
        table_description = "权限表"
