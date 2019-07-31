from django.db import models
from django.utils import timezone


class Report(models.Model):
    firstoccurrence = models.DateTimeField()
    node = models.CharField(max_length=50)
    severity = models.CharField(max_length=20)
    alarm = models.TextField()

    def __str__(self):
        return self.alarm
