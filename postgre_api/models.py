from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255, default="john")
    surname = models.CharField(max_length=255, default="doe")
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    age = models.IntegerField()
    weight = models.FloatField()
    height = models.FloatField()
    profession = models.CharField(max_length=255)

