from django.db import models


# Create your models here.

class Human(models.Model):
    name = models.CharField(max_length=50)
    family = models.CharField(max_length=50)
    age = models.IntegerField()
    address = models.TextField()
    register_date = models.DateTimeField()

