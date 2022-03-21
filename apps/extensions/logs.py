# -*- encoding: utf-8 -*-
'''
@File    :   log.py
@Time    :   2022/02/10 11:23:16
@Author  :   sk 
@Version :   1.0
@Contact :   ldu_sunkaixuan@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
'''

# here put the import lib

__all__ = ['logger']

import sys

from loguru import logger

# TODO: 需要继续重新构造

logconfig = {
    'handlers': [
        {'sink': sys.stdout, 'level': 'DEBUG', 'backtrace':True, 'diagnose':True, 'enqueue': True}
    ]
}


def to_configure_loguru(logger, config: dict):

    logger.configure(**config)

    return logger


logger.remove()

logger = to_configure_loguru(logger, logconfig)


