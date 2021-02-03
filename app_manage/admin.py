from django.contrib import admin
from app_manage.models import Project
from app_manage.models import Module
# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    """项目管理"""
    list_display = ['project_name', 'project_status', 'project_describe', 'create_time']  # 显示字段
    search_fields = ['project_name']  # 搜索栏
    list_filter = ['project_status']  # 过滤器


class ModuleAdmin(admin.ModelAdmin):
    """模块管理"""
    list_display = ['project', 'module_name', 'module_describe', 'create_time']  # 显示字段


admin.site.register(Project, ProjectAdmin)
admin.site.register(Module, ModuleAdmin)
