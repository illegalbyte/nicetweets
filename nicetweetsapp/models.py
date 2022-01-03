from django.db import models
from django.conf import settings
from django.utils import timezone


# Create your models here.

class Tweet(models.Model):
    text = models.CharField(max_length=400)
    sentiment = models.FloatField(default=0.0)
    created_at = models.DateTimeField(default=timezone.now)

    def store(self):
        self.save()

    def __str__(self):
        return self.text

    