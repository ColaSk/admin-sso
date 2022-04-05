import traceback

from apps.extensions.logs import logger
from apps.extensions.response import ErrorResponse
from fastapi import Request
from fastapi.exceptions import RequestValidationError
from starlette.exceptions import HTTPException as StarletteHTTPException
from starlette.responses import JSONResponse
from .status import status


async def default_exception_handler(request: Request, exc: Exception) -> JSONResponse:

    # TODO: 异常记录

    logger.error(traceback.format_exc())

    responce = ErrorResponse(
        code=status.HTTP_500_INTERNAL_SERVER_ERROR, 
        massage=exc.__str__())

    return JSONResponse(content=responce.dict(), status_code=responce.code)


async def define_http_exception_handler(
    request: Request, exc: StarletteHTTPException
) -> JSONResponse:

    logger.error(traceback.format_exc())

    headers = getattr(exc, "headers", None)

    responce = ErrorResponse(code=exc.status_code, massage={"detail": exc.detail})

    return JSONResponse(responce.dict(), status_code=exc.status_code, headers=headers)


async def define_request_validation_error(
    request: Request, exc: RequestValidationError
) -> JSONResponse:

    logger.error(traceback.format_exc())

    responce = ErrorResponse(massage=exc.errors(), code=422)

    return JSONResponse(responce.dict(), status_code=responce.code)
