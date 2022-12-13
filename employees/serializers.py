from rest_framework import serializers

from .models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = [
            'user',
            'branch_id',
            'designation',
            'address',
            'contact'
        ]
