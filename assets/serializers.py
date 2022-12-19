from rest_framework import serializers

from .models import Asset


class AssetSerializer(serializers.ModelSerializer):
    # location = serializers.SerializerMethodField('get_asset_name')

    class Meta:
        model = Asset
        fields = [
            "asset_name",
            "serial_number",
            "model",
            "company",
            "image_url",
            "status",
        ]

        # def get_asset_name(self, obj):
        #     return obj.asset_name
