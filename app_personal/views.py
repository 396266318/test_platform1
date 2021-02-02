from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import auth
from django.contrib.auth.decorators import login_required
# Create your views here.


def hello(request):
    return render(request, 'hello.html')


def login(request):
    """用户登录"""
    if request.method == "GET":
        return render(request, 'login.html')

    if request.method == "POST":
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        if username == "" or password == "":
            return render(request, "login.html", {"error": "用户名或密码为空！"})

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)  # 记录用户的登录状态
            response = HttpResponseRedirect("hello")
            response.set_cookie("user", username, 3600)
            return response
        else:
            return render(request, "login.html", {"error": "用户名或密码错误！"})


@login_required
def logout(request):
    """用户退出"""
    auth.logout(request)
    return HttpResponseRedirect("/")