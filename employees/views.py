from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Employee
from .serializers import EmployeeSerializer

# Create your views here.


@api_view(['GET'])
def employee_view(request, pk=None, *args, **kwargs):

    try:
        qs = Employee.objects.all()
        data = EmployeeSerializer(qs, many=True).data
        return Response({
            'data': [data],
            'errors': [],
        }, status=status.HTTP_200_OK)

    except Exception as e:
        e = str(e)

        return Response({
            'data': [],
            'errors': [e],
        }, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def employee_details_view(request, *args, **kwargs):

    try:
        qs = Employee.objects.get(pk=kwargs['pk'])
        data = EmployeeSerializer(qs).data
        return Response({
            'data': [data],
            'errors': [],
        }, status=status.HTTP_200_OK)

    except Exception as e:
        e = str(e)

        return Response({
            'data': [],
            'errors': [e],
        }, status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_employee_view(request, *args, **kwargs):

    try:
        serializer = EmployeeSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            designation = serializer.validated_data.get('designation')
            address = serializer.validated_data.get('address')
            contact = serializer.validated_data.get('contact')
            user = serializer.validated_data.get('user')
            branch_id = serializer.validated_data.get('branch_id')

            serializer.save(designation=designation, address=address,
                            contact=contact, user=user, branch_id=branch_id)
            return Response({
                'data': [serializer.data],
                'errors': [],
            }, status=status.HTTP_200_OK)

    except Exception as e:
        e = str(e)

        return Response({
            'data': [],
            'errors': [e],
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
