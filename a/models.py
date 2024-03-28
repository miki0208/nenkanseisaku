from django.db import models

# Create your models here.

class Tweet(models.Model):
    message = models.CharField(max_length=200)
    name = models.CharField(max_length=200)

class Page(models.Model):
    message = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    votes = models.IntegerField(default=0)