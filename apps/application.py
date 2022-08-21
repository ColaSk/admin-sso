from . import create_app
from config import setting, ORM_LINK_CONF
from apps.admin.urls import api_router as admin_router
from apps.exceptions import exception_handlers
from apps.extensions.depends import dependencies
from fastapi import FastAPI


routers = {"v2": (admin_router,)}

app: FastAPI = create_app(
    config=setting.app.dict(),
    routers=routers,
    handlers=exception_handlers,
    dependencies=dependencies,
    # middlewares=app_middleware,
    db_config=ORM_LINK_CONF,
)
