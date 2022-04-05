from typing import Any, Dict, Optional
from fastapi.exceptions import HTTPException
from .status import status


class ExceptionBase(HTTPException):
    def __init__(
        self,
        status_code: int = 0,
        detail: Any = None,
        headers: Optional[Dict[str, Any]] = None,
    ):

        if not status_code:
            status_code = getattr(self, "STATUS_CODE", status_code)

        if not detail:
            detail = getattr(self, "DETAIL", status_code)

        super().__init__(status_code, detail, headers)


class BadRequest(ExceptionBase):
    STATUS_CODE: int = status.HTTP_400_BAD_REQUEST
    DETAIL: Any = "bad request"


class Forbidden(ExceptionBase):
    STATUS_CODE: int = status.HTTP_403_FORBIDDEN
    DETAIL: Any = "forbidden"


class NotFound(ExceptionBase):
    STATUS_CODE: int = status.HTTP_404_NOT_FOUND
    DETAIL: Any = "not found"


class Gone(ExceptionBase):
    STATUS_CODE: int = status.HTTP_410_GONE
    DETAIL: Any = "gone"


class GoneException(ExceptionBase):
    STATUS_CODE: int = status.HTTP_410_GONE
    DETAIL: Any = "gone"


class UnprocessableEntity(ExceptionBase):
    STATUS_CODE: int = status.HTTP_422_UNPROCESSABLE_ENTITY
    DETAIL: Any = "unprocessable entity"
