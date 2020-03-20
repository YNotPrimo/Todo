from django.db import models


# Create your models here.
class TodoModel(models.Model):
    title = models.CharField(max_length=10)
    description = models.TextField(max_length=100)
    is_done = models.BooleanField(default=False)
