#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
auto: xuan
DATA: 2021/1/25 9:05 下午 
"""
from django.urls import path
from app_manage.views import project_view, module_view


urlpatterns = [
    # 项目管理
    path('', project_view.list_project),
    path('project_list/', project_view.list_project),                # 项目列表
    path('project_add/', project_view.add_project),                  # 添加项目
    path('project_edit/<int:pid>/', project_view.edit_project),      # 编辑项目
    path('project_delete/<int:pid>/', project_view.delete_project),  # 删除项目

    # 模块管理
    path('module_list/', module_view.list_module),                   # 模块列表
    path('module_add/', module_view.add_module),                     # 创建模块
    path('module_edit/<int:mid>', module_view.edit_module),          # 编辑模块
    path('module_delete/', module_view.delete_module),               # 删除模块
]