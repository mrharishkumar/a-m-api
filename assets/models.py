from django.db import models

# Create your models here.


class Asset(models.Model):
    serial_number = models.CharField(primary_key=True, max_length=40)
    asset_name = models.CharField(max_length=20)
    model = models.CharField(max_length=20)
    company = models.CharField(max_length=50)
    image_url = models.CharField(max_length=100, blank=True, null=True)
