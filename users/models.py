from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
"""
Used https://www.youtube.com/watch?v=1BeZxMbSZNI&list=PLgjw1dR712jqq75ZDdow9Cx0L2ahUaE6G&index=4 
to complete assignment
"""


class CustomUser(AbstractUser):
    homepage = models.URLField(null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    display_name = models.CharField(max_length=30)

    def __str__(self):
        return self.display_name
