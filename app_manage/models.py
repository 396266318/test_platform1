from django.db import models

# Create your models here.


class Project(models.Model):
    """
    项目表
    """
    project_name = models.CharField("项目名称", max_length=100, null=False, default="")
    project_describe = models.TextField("项目描述", default="")
    project_status = models.BooleanField("项目状态", default=True)
    update_time = models.DateTimeField("更新时间", auto_now=True)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)

    def __str__(self):
        return self.project_name


class Module(models.Model):
    """
    模块表
    """
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    module_name = models.CharField("模块名称", max_length=100, null=False, default="")
    module_describe = models.TextField("模块描述", default="")
    update_time = models.DateTimeField("更新时间", auto_now=True)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)

    def __str__(self):
        return self.module_name
