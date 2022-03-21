from .setting import get_setting, TortoiseORMSetting

setting = get_setting('config/config.toml')

print(setting)

ORM_LINK_CONF = TortoiseORMSetting(db_config=setting.db).orm_link_config