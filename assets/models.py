from django.db import models

# Create your models here.


class AssetStatus(models.TextChoices):
    AVAILABLE = 'AVAILABLE'
    UNAVAILABLE = 'UNAVAILABLE'


class Asset(models.Model):
    serial_number = models.CharField(primary_key=True, max_length=40)
    asset_name = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    company = models.CharField(max_length=50)
    image_url = models.CharField(max_length=150, blank=True, null=True)
    status = models.CharField(max_length=15,choices=AssetStatus.choices,default=AssetStatus.AVAILABLE)
