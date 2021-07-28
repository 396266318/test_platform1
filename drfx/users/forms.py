from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    """自定义用户创建表格"""

    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):
    """自定义用户更改表格"""

    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
