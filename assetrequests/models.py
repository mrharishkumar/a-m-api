from django.db import models
from assets.models import Asset
from employees.models import Employee

# Create your models here.


class Status(models.TextChoices):
    GRANTED = 'GRANTED'
    DENIED = 'DENIED'
    PENDING = 'PENDING'


class AssetRequest(models.Model):
    asset_id = models.ForeignKey(Asset, on_delete=models.CASCADE)
    employee_id = models.ForeignKey(Employee, on_delete=models.CASCADE)
    remarks = models.TextField(max_length=100)
    status = models.CharField(
        max_length=10, choices=Status.choices, default=Status.PENDING)