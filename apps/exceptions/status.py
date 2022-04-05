# -*- encoding: utf-8 -*-
"""
@File    :   status.py
@Time    :   2022/04/04 23:36:42
@Author  :   KX
@Version :   1.0
@Contact :   ldu_sunkaixuan.163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
"""

# here put the import lib
from fastapi import status as status

"""自定义状态码
支持所有 fastapi 状态码

含义:
    1xx: 相关信息
    2xx: 操作成功
    3xx: 重定向
    4xx: 客户端错误
    5xx: 服务器错误
"""
