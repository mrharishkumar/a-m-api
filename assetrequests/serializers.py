from rest_framework import serializers
from .models import User

from .models import AssetRequest


class AssetRequestSerializer(serializers.ModelSerializer):

    class Meta:
        model = AssetRequest
        fields = [
            "id",
            "asset_id",
            "employee_id",
            "remarks",
            "status",
        ]


class UserSerializer(serializers.Serializer):
    class Meta:
        model = User
        fields = ('username', 'email')