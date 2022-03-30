from tortoise.models import Model
from tortoise import fields
from passlib.context import CryptContext
from .mixin import ModelBase, DelModelBase, TimeModelBase, ModelMixin

class User(ModelBase, DelModelBase, TimeModelBase, ModelMixin):

    name = fields.CharField(max_length=255, null=False, description='name')
    pwd = fields.CharField(max_length=255, null=False, description='password hash')
    phone = fields.CharField(max_length=255, null=False, unique=True, description='phone')
    email = fields.CharField(max_length=255, description='email')

    class Meta:
        table = 'users'
        table_description = '用户表'

    @property
    def pwdcontext(self):
        return CryptContext(schemes=["bcrypt"], deprecated="auto")

    @property
    def password(self):
        return self.pwd

    @password.setter
    def password(self, value):
        self.pwd = self.pwdcontext.hash(value)

    def check_password(self, password: str) -> bool:
        return self.pwdcontext.verify(password, self.password)


class Role(ModelBase, DelModelBase, TimeModelBase, ModelMixin):
    
    name = fields.CharField(max_length=255, null=False, description='name')
    desc = fields.TextField(description='desc')

    class Meta:
        table = 'roles'
        table_description = '角色表'


class Permission(ModelBase, DelModelBase, TimeModelBase, ModelMixin):
    
    name = fields.CharField(max_length=255, null=False, description='name')
    desc = fields.TextField(description='desc')
    
    class Meta:
        table = 'permission'
        table_description = '权限表'