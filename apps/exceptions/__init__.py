from .handlers import (default_exception_handler, 
                       define_http_exception_handler, 
                       define_request_validation_error)
from starlette.exceptions import HTTPException as StarletteHTTPException
from fastapi.exceptions import RequestValidationError

exception_handlers = {
    Exception: default_exception_handler,
    StarletteHTTPException: define_http_exception_handler,
    RequestValidationError: define_request_validation_error
}