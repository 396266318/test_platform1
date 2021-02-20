from rest_framework import serializers
from . import models


class UserSerializer(serializers.ModelSerializer):
    """用户序列化"""

    class Meta:
        model = models.CustomUser
        fields = ('email', 'username', )