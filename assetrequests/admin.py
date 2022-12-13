from django.contrib import admin

from .models import AssetRequest

# Register your models here.

@admin.register(AssetRequest)
class AssetRequestAdmin(admin.ModelAdmin):
    list_display=['asset_id','employee_id','remarks','status']
