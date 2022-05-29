
from django.db import models

class Familiares(models.Model):
    name = models.CharField(max_length=40)
    age = models.IntegerField()

