#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
auto: xuan
DATA: 2021/2/18 5:27 下午 
"""
from django.urls import path
from app_case import views


urlpatterns = [
    path('', views.list_case),                             # 用例页面
    path('add_case/', views.add_case),                     # 添加用例
    path('edit_case/<int:cid>', views.edit_case),          # 编辑用例
    path('send_req/', views.send_case),                    # 发送接口请求
    path('assert_result/', views.assert_result),           # 断言结果
    path('save_case/', views.save_case),                   # 保存用例
    path('delete_case/', views.delete_case),               # 删除用例

    path('get_case_info/', views.get_case_info),           # 获取接口数据
]