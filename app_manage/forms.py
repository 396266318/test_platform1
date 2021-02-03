#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
auto: xuan
DATA: 2021/1/25 9:42 下午 
"""
from django import forms
from django.forms import widgets
from app_manage.models import Project, Module


class ProjectForm(forms.Form):
    """项目表单"""
    project_name = forms.CharField(label="名称", max_length=100, widget=widgets.TextInput(attrs={'class': "form-control"}))
    project_describe = forms.CharField(label="描述", widget=widgets.TextInput({"class": "form-control"}))
    project_status = forms.BooleanField(label="状态", widget=widgets.CheckboxInput())


class ProjectEditForm(forms.ModelForm):
    """编辑项目表单"""
    class Meta:
        model = Project
        fields = ['project_name', 'project_describe', 'project_status']


class ModuleForm(forms.ModelForm):
    """模块表单"""
    class Meta:
        model = Module
        fields = ['project', 'module_name', 'module_describe']
