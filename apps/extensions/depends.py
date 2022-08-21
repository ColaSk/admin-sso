from typing import Optional
from fastapi import Cookie, Header, Depends


class HeaderDependBase(object):

     def __init__(
        self,
        content_type: Optional[str] = Header(None),
        content_length: Optional[str] = Header(None),
        host: Optional[str] = Header(None),
        user_agent: Optional[str] = Header(None),
        accept: Optional[str] = Header(None),
        accept_encoding: Optional[str] = Header(None),
        connection: Optional[str] = Header(None)
    ):

        self.content_type = content_type
        self.content_length = content_length
        self.host = host
        self.user_agent = user_agent
        self.accept = accept
        self.accept_encoding = accept_encoding
        self.connection = connection


class CookieDependBase(object):

    def __init__(self): pass


class GlobalHeaderDepend(HeaderDependBase):

    def __init__(self):
        super().__init__()



async def app_depend(
    header: HeaderDependBase = Depends(HeaderDependBase),
):
    # TODO: 处于测试阶段，后续将进行扩展
    print(header.__dict__)

# 全局依赖项
dependencies = [Depends(app_depend)]