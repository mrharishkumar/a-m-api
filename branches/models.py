from django.db import models

# Create your models here.


class Branch(models.Model):
    address = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
