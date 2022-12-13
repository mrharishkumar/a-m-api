from django.contrib import admin
from .models import Asset

# Register your models here.
@admin.register(Asset)
class AssetAdmin(admin.ModelAdmin):
    list_display=['serial_number','asset_name','model','company', 'image_url']