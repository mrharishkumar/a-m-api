from django.db import models
from django.contrib.auth.models import User
from branches.models import Branch

# Create your models here.


class Employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    branch_id = models.ForeignKey(Branch, on_delete=models.CASCADE)
    designation = models.CharField(max_length=20)
    address = models.CharField(max_length=40)
    contact = models.CharField(max_length=10)
