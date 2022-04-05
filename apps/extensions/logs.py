# -*- encoding: utf-8 -*-
"""
@File    :   log.py
@Time    :   2022/02/10 11:23:16
@Author  :   sk 
@Version :   1.0
@Contact :   ldu_sunkaixuan@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
"""

# here put the import lib

__all__ = ["logger"]

import sys
import os
from loguru import logger


def env(key, type_, default=None):
    if key not in os.environ:
        return default

    val = os.environ[key]

    if type_ == str:
        return val
    elif type_ == bool:
        if val.lower() in ["1", "true", "yes", "y", "ok", "on"]:
            return True
        if val.lower() in ["0", "false", "no", "n", "nok", "off"]:
            return False
        raise ValueError(
            "Invalid environment variable '%s' (expected a boolean): '%s'" % (key, val)
        )
    elif type_ == int:
        try:
            return int(val)
        except ValueError:
            raise ValueError(
                "Invalid environment variable '%s' (expected an integer): '%s'"
                % (key, val)
            ) from None


class defaults(object):

    LOGURU_AUTOINIT = env("LOGURU_AUTOINIT", bool, True)

    LOGURU_FORMAT = env(
        "LOGURU_FORMAT",
        str,
        (
            "<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> | "
            "<yellow>{level: <8}</yellow> | "
            "<cyan>{name}</cyan>:<cyan>{function}</cyan>:<cyan>{line}</cyan> - "
            "<level>{message}</level>"
        ),
    )
    LOGURU_FILTER = env("LOGURU_FILTER", str, None)
    LOGURU_LEVEL = env("LOGURU_LEVEL", str, "DEBUG")
    LOGURU_COLORIZE = env("LOGURU_COLORIZE", bool, None)
    LOGURU_SERIALIZE = env("LOGURU_SERIALIZE", bool, False)
    LOGURU_BACKTRACE = env("LOGURU_BACKTRACE", bool, True)
    LOGURU_DIAGNOSE = env("LOGURU_DIAGNOSE", bool, True)
    LOGURU_ENQUEUE = env("LOGURU_ENQUEUE", bool, False)
    LOGURU_CATCH = env("LOGURU_CATCH", bool, True)

    LOGURU_TRACE_NO = env("LOGURU_TRACE_NO", int, 5)
    LOGURU_TRACE_COLOR = env("LOGURU_TRACE_COLOR", str, "<cyan><bold>")
    LOGURU_TRACE_ICON = env("LOGURU_TRACE_ICON", str, "✏️")  # Pencil

    LOGURU_DEBUG_NO = env("LOGURU_DEBUG_NO", int, 10)
    LOGURU_DEBUG_COLOR = env("LOGURU_DEBUG_COLOR", str, "<blue><bold>")
    LOGURU_DEBUG_ICON = env("LOGURU_DEBUG_ICON", str, "🐞")  # Lady Beetle

    LOGURU_INFO_NO = env("LOGURU_INFO_NO", int, 20)
    LOGURU_INFO_COLOR = env("LOGURU_INFO_COLOR", str, "<bold>")
    LOGURU_INFO_ICON = env("LOGURU_INFO_ICON", str, "ℹ️")  # Information

    LOGURU_SUCCESS_NO = env("LOGURU_SUCCESS_NO", int, 25)
    LOGURU_SUCCESS_COLOR = env("LOGURU_SUCCESS_COLOR", str, "<green><bold>")
    LOGURU_SUCCESS_ICON = env("LOGURU_SUCCESS_ICON", str, "✔️")  # Heavy Check Mark

    LOGURU_WARNING_NO = env("LOGURU_WARNING_NO", int, 30)
    LOGURU_WARNING_COLOR = env("LOGURU_WARNING_COLOR", str, "<yellow><bold>")
    LOGURU_WARNING_ICON = env("LOGURU_WARNING_ICON", str, "⚠️")  # Warning

    LOGURU_ERROR_NO = env("LOGURU_ERROR_NO", int, 40)
    LOGURU_ERROR_COLOR = env("LOGURU_ERROR_COLOR", str, "<red><bold>")
    LOGURU_ERROR_ICON = env("LOGURU_ERROR_ICON", str, "❌")  # Cross Mark

    LOGURU_CRITICAL_NO = env("LOGURU_CRITICAL_NO", int, 50)
    LOGURU_CRITICAL_COLOR = env("LOGURU_CRITICAL_COLOR", str, "<RED><bold>")
    LOGURU_CRITICAL_ICON = env(
        "LOGURU_CRITICAL_ICON", str, "☠️"
    )  # Skull and Crossbones

    LOGURU_BASE_DIR = os.path.dirname(
        os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    )
    LOGURU_FILE_PATH = f"{LOGURU_BASE_DIR}/logs"


log_default_config = {
    "handlers": [
        {
            "sink": sys.stdout,
            "level": defaults.LOGURU_LEVEL,
            "enqueue": True,
            "colorize": True,
            "format": defaults.LOGURU_FORMAT,
        },
        {
            "sink": f"{defaults.LOGURU_FILE_PATH}/main.log",
            "level": defaults.LOGURU_LEVEL,
            "encoding": "utf-8",
            "rotation": "00:00",
            "compression": "zip",
            "backtrace": defaults.LOGURU_BACKTRACE,
            "diagnose": defaults.LOGURU_DIAGNOSE,
            "enqueue": defaults.LOGURU_ENQUEUE,
            "colorize": defaults.LOGURU_COLORIZE,
            "format": defaults.LOGURU_FORMAT,
        },
    ],
    "levels": None,
    "extra": None,
    "patcher": None,
    "activation": None,
}


def to_configure_loguru(logger: logger.__class__, config: dict = log_default_config):
    """重新配置logger"""

    logger.remove()
    logger.configure(**config)

    return logger


logger = to_configure_loguru(logger)
