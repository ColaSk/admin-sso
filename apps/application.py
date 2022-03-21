from . import create_app
from config import setting, ORM_LINK_CONF
from apps.admin.urls import api_router

app = app = create_app(
    config=setting.app.dict(),
    routers={'v2': (api_router, )}, 
    # handlers=exception_handlers,
    # dependencies=dependencies,
    # middlewares=app_middleware,
    db_config=ORM_LINK_CONF
)