from typing import List
from .schemas import UserCreate
from apps.models.models import User
class UserOperator(object):

    @classmethod
    async def login(cls, user): ...


    @classmethod
    async def create(cls, userdata: UserCreate) -> User:
        user = User(name=userdata.username)
        user.password = userdata.password # 密码哈希
        await user.save()
        return user
    
    @classmethod
    async def list(cls) -> List[User]:
        users = await User.all()
        return users

