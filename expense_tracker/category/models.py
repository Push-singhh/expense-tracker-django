from django.db import models

from users.models import CustomUser


class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, null=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
