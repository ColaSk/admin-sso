# -*- encoding: utf-8 -*-
"""
@File    :   route.py
@Time    :   2022/03/21 18:17:15
@Author  :   sk
@Version :   1.0
@Contact :   ldu_sunkaixuan@163.com
@License :   (C)Copyright 2017-2018, Liugroup-NLPR-CASIA
@Desc    :   None
"""

# here put the import lib

from datetime import datetime
from fastapi import Request
from fastapi.routing import APIRoute

from .logs import logger


class LoggingRoute(APIRoute):
    """Extension Route and log request.json()"""

    def get_route_handler(self):

        original_route_handler = super().get_route_handler()

        async def log_request_detail(request: Request):

            start_time = datetime.now()
            id = int(start_time.timestamp() * (10**6))

            logger.info(f"{id} start request: time: {start_time}".center(125, "*"))
            logger.info(f"{request.method} {request.url}")

            content_type = request.headers.get("content-type", "")

            if "application/json" in content_type:
                params = await request.json()
            elif "multipart/form-data" in content_type:
                params = await request.form()
            else:
                params = None

            logger.info(f"content_type: {content_type}, params: {params}")

            result = await original_route_handler(request)

            end_time = datetime.now()
            runtime = (end_time - start_time).total_seconds()

            logger.info(
                f"{id} end request: {end_time}, runtime: {runtime}".center(125, "*")
            )

            return result

        return log_request_detail
