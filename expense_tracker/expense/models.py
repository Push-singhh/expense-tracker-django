from datetime import datetime

from django.db import models
from category.models import Category
from users.models import CustomUser


class Expense(models.Model):
    amount = models.BigIntegerField()
    category = models.ForeignKey(Category, on_delete=models.Empty)
    created_at = models.DateTimeField(default=datetime.now)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
