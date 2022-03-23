from typing import Any, Optional
from pydantic import BaseModel

class BaseResponse(BaseModel):
    success: bool = True
    code: int = 200
    massage: Any = None
    data: Any = None


class NormalResponse(BaseResponse):
    data: Optional[str] = 'success'


class SuccessResponse(BaseResponse): ...


class ErrorResponse(BaseResponse):
    success: bool = False
    code: int = 500
