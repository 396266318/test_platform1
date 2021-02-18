#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
auto: xuan
DATA: 2021/1/25 9:53 下午 
"""
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from app_manage.models import Project, Module
from app_manage.forms import ProjectForm, ProjectEditForm, ModuleForm


def list_module(request):
    """模块列表"""
    module_list = Module.objects.all()
    return render(request, "module/list.html", {"modules": module_list})


def add_module(request):
    """创建模块"""
    if request.method == "POST":
        form = ModuleForm(request.POST)
        if form.is_valid():
            project = form.cleaned_data['project']
            name = form.cleaned_data['module_name']
            describe = form.cleaned_data['module_describe']
            Module.objects.create(module_name=name, module_describe=describe, project=project)

        return HttpResponseRedirect("/manage/module_list/")
    else:
        form = ModuleForm()
    return render(request, 'module/add.html', {"form": form})


def edit_module(request, mid):
    """编辑模块"""
    if request.method == "POST":
        form = ModuleForm(request.POST)
        if form.is_valid():
            project = form.cleaned_data['project']
            name = form.cleaned_data['module_name']
            describe = form.cleaned_data['module_describe']

            m = Module.objects.get(id=mid)
            m.project = project
            m.name = name
            m.describe = describe
            m.save()
        return HttpResponseRedirect('/manage/module_list/')
    else:
        if mid:
            m = Module.objects.get(id=mid)
            form = ModuleForm(instance=m)
        else:
            form = ModuleForm()
        return render(request, 'module/edit.html', {"form": form, "id": mid})


def delete_module(request, mid):
    """删除模块"""
    if request.method == "GET":
        m = Module.objects.get(id=mid)
        m.delete()
        return HttpResponseRedirect("/manage/module_list/")
    else:
        return HttpResponseRedirect("/manage/module_list/")
