# -*- encoding: utf-8 -*-

import os
from typing import Optional, Dict, Union, Any
from pydantic import BaseModel
import pytomlpp

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class JWTConfig(BaseModel):
    secret_key: str = "23bec386829bd6688b9940534113db03592ed7e5f70aa3a509a5a1d3f135a1e9"
    algorithm: str = "HS256"
    token_expires_m: int = 30


class DBConfig(BaseModel):
    
    host: Optional[str] = '127.0.0.1'
    port: Optional[int] = 3306
    database: str
    user: str
    pwd: str


class LogConfig(BaseModel):
    level: str = 'DEBUG'
    logfile: Optional[str] = None


class AppConfig(BaseModel):

    title: Optional[str] = 'FastAPI'
    description: Optional[str] = ''
    version: Optional[str] = "1.0.0"
    license_info: Optional[Dict[str, Union[str, Any]]] = {}
    contact: Optional[Dict[str, Union[str, Any]]] = {}


class Setting(BaseModel):

    db: DBConfig
    app: AppConfig
    jwt: JWTConfig = None


class TortoiseORMSetting(BaseModel):

    db_config: DBConfig

    def _get_base_config(self, apps: dict) -> dict:

        return {
            "connections": {
                "default": {
                    "engine": "tortoise.backends.mysql",
                    "credentials": {
                        "host": self.db_config.host,
                        "port": self.db_config.port,
                        "database": self.db_config.database,
                        "user": self.db_config.user,
                        "password": self.db_config.pwd,
                        'charset': 'utf8mb4',
                    }
                }
            },
            "apps": apps,
            "use_tz": False,
            'timezone': 'Asia/Shanghai'
        } 
    
    @property
    def orm_link_config(self) -> dict:

        orm_apps_setting = {
             'models': {
                'models': [
                    'aerich.models',
                    # 'apps.models.models'
                ],
                'default_connection': 'default',
            }
        }

        return self._get_base_config(orm_apps_setting)


def get_setting(confile: str) -> Setting:

    path = os.path.join(BASE_DIR, confile)
    conf = pytomlpp.load(path)
    return Setting.parse_obj(conf)


