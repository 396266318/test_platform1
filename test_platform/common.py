#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
auto: xuan
DATA: 2021/2/18 11:51 上午 
"""
from django.http import JsonResponse


def response(status=None, message=None, data=[]):
    """通用的接口返回"""
    if status is None:
        status = 10200
    if message is None:
        message = "成功"

    return JsonResponse(
        {"status": status, "message": message, "data": data}
    )

