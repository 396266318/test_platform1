#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
auto: xuan
DATA: 2021/1/25 9:53 下午 
"""
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from app_manage.models import Project
from app_manage.forms import ProjectForm, ProjectEditForm


@login_required
def list_project(request):
    """项目清单"""
    username = request.COOKIES.get('user', '')
    project_list = Project.objects.all()
    return render(request, "project/list.html", {"projects": project_list, "user": username})


def add_project(request):
    """创建项目"""
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            describe = form.cleaned_data["describe"]
            status = form.cleaned_data["status"]
            print("状态", status, type(status))
            Project.objects.create(project_name=name, project_describe=describe, project_status=status)
        return HttpResponseRedirect('/manage/')
    else:
        form = ProjectForm()
    return render(request, 'project/add.html', {"form": form})


def edit_project(request, pid):
    """编辑项目"""
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data["project_name"]
            describe = form.cleaned_data["project_describe"]
            status = form.cleaned_data["project_status"]

            p = Project.objects.get(id=pid)
            p.project_name = name
            p.project_describe = describe
            p.project_status = status
            print(p.project_name, p.project_describe)
            p.save()
        return HttpResponseRedirect("/manage/")
    else:
        if pid:
            p = Project.objects.get(id=pid)
            form = ProjectEditForm(instance=p)
        else:
            form = ProjectForm()
        return render(request, "project/edit.html", {"form": form, "id": pid})


def delete_project(request, pid):
    """删除项目"""
    if request.method == "GET":
        p = Project.objects.get(id=pid)
        p.delete()
        return HttpResponseRedirect("/manage/")
    else:
        return HttpResponseRedirect("/manage/")
