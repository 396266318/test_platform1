#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
auto: xuan
DATA: 2021/2/18 11:48 上午 
"""
from django.urls import path
from app_variable import views


urlpatterns = [
    # 变量管理
    path("", views.variable_list),
    path("save_variable/", views.save_variable)
]
