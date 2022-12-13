from rest_framework import serializers

from .models import AssetRequest


class AssetRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = AssetRequest
        fields = [
            "asset_id",
            "employee_id",
            "remarks",
            "status",
        ]
