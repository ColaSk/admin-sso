from typing import List
from apps.models.models import User


"""
# TODO: 将会删除
"""


class UserOperator(object):
    @classmethod
    async def list(cls) -> List[User]:
        users = await User.all()
        return users
