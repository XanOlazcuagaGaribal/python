from django.db import models

class Task(models.Model):
    content = models.CharField(max_length=200)
    is_done = models.BooleanField()
    created_date = models.DateField()