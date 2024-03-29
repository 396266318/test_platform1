"""test_platform URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from app_personal import views as personal_views
from app_manage import views as manage_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', personal_views.hello),

    # 账户管理
    path('', personal_views.login),
    path('login/', personal_views.login),
    path('logout/', personal_views.logout),

    # 项目管理
    path('manage/', include('app_manage.urls')),

    # 用例管理
    path('case/', include('app_case.urls')),

    # 任务管理
    path("task/", include("app_task.urls")),

    # 变量管理
    path('variable/', include('app_variable.urls'))
]
