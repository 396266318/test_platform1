from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class CustomUser(AbstractUser):
    """自定义用户"""

    name = models.CharField(blank=True, max_length=255)

    def __str__(self):
        return self.email
