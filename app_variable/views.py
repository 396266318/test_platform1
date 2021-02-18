from django.shortcuts import render
from app_variable.models import Variable
from test_platform.common import response
# Create your views here.


def variable_list(request):
    """变量列表"""
    variable = Variable.objects.all()
    return render(request, "variable/list.html", {"variable": variable})


def save_variable(request):
    """保存变量"""
    if request.method == "POST":
        vid = request.POST.get("vid", "")
        key = request.POST.get("key", "")
        value = request.POST.get("value", "")
        desc = request.POST.get("desc", "")

        if key == "" or value == "":
            return response(10102, "必传参数为空")

        if vid == "0":
            Variable.objects.create(key=key, value=value, describe=desc)
            return response()

        else:
            variable = Variable.objects.get(id=vid)
            variable.key = key
            variable.value = value
            variable.describe = desc
            variable.save()
            return response()
    else:
        return response(10101, "请求方法错误")

