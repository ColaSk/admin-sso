from .handlers import default_exception_handler, define_http_exception_handler
from tortoise.exceptions import IntegrityError
from starlette.exceptions import HTTPException as StarletteHTTPException

exception_handlers = {
    Exception: default_exception_handler,
    StarletteHTTPException: define_http_exception_handler
}