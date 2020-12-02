from django.db import models

# Create your models here.

class Task(models.Model):
    content = models.CharField(max_length=200)
    is_done = models.BooleanField()
    created_date = models.DateTimeField("Date create")