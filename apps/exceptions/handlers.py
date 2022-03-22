import traceback
from fastapi import Request
from starlette.responses import JSONResponse
from apps.extensions.response import ErrorResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exception_handlers import http_exception_handler

from apps.extensions.logs import logger

async def default_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    
    # TODO: 异常记录

    logger.error(traceback.format_exc())

    responce = ErrorResponse(code=500, massage=exc.__str__())

    return JSONResponse(
        content=responce.dict(),
        status_code=responce.code
    )

async def define_http_exception_handler(request: Request, exc: StarletteHTTPException) -> JSONResponse:

    logger.error(traceback.format_exc())
    
    headers = getattr(exc, "headers", None)
    
    responce = ErrorResponse(
        code=exc.status_code, 
        massage={"detail": exc.detail})


    if headers:
        return JSONResponse(
            responce.dict(), status_code=exc.status_code, headers=headers
        )
    else:
        return JSONResponse(responce.dict(), status_code=exc.status_code)
