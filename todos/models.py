from django.db import models


# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    is_complete = models.BooleanField(default=False)
