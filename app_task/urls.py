#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
auto: xuan
DATA: 2021/2/20 11:02 下午 
"""
from django.urls import path
from app_task import views


urlpatterns = [
    # 任务管理
    path("", views.task_list),
    path("case/node/", views.case_node),
    path("add/", views.task_add),
    path("edit/<int:tid>/", views.task_edit),
    path("save_task/", views.task_save),

    path("run_task/<int:tid>/", views.task_rung),
    path("log/<int:tid>/", views.log_list),

    path("get_log/", views.get_log)
]