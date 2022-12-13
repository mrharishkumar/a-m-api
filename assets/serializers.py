from rest_framework import serializers

from .models import Asset


class AssetSerializer(serializers.ModelSerializer):

    class Meta:
        model = Asset
        fields = [
            "asset_name",
            "serial_number",
            "model",
            "company",
            "image_url",
        ]

