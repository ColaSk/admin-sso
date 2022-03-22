from typing import Any, Optional
from pydantic import BaseModel

class BaseResponse(BaseModel):
    success: bool = True
    code: int = 200
    massage: str = None
    data: Any = None


class NormalResponse(BaseResponse):
    data: Optional[str] = 'success'

