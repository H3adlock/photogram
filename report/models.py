from django.db import models
from django.utils import timezone


class Report(models.Model):
    firstoccurrence = models.DateTimeField()
    node = models.CharField(max_length=50)
    severity = models.CharField(max_length=20)
    alarm = models.TextField()
    slug = models.SlugField(null=True, default='')
    char = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.alarm
