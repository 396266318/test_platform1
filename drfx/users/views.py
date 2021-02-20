from django.shortcuts import render
from rest_framework import generics
from . import models
from . import serializers
# Create your views here.


class UserListView(generics.ListAPIView):
    """用户列表视图"""
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer

