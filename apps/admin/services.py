from typing import List, Tuple
from .schemas import UserCreate, UserLogin
from apps.models.models import User
from apps.modules.user import CurrUser
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends


oauth2_scheme = OAuth2PasswordBearer('/api/v2/users/login')

class UserOperator(object):

    @classmethod
    async def login(cls, user: UserLogin) -> Tuple[str, dict]:
        return await CurrUser.login(user.username, user.password)

    @classmethod
    async def curr_user(cls, token: str = Depends(oauth2_scheme)) -> CurrUser:
        print(token)
        return await CurrUser.get_obj_by_token(token)

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

