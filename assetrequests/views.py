from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import AssetRequest
from .serializers import AssetRequestSerializer

# Create your views here.


@api_view(['GET'])
def asset_request_list_view(request, *args, **kwargs):

    try:
        qs = AssetRequest.objects.all()
        data = AssetRequestSerializer(qs, many=True).data
        return Response({
            'data': data,
            'error': [],
        }, status=status.HTTP_200_OK)

    except Exception as e:
        e = str(e)

        return Response({
            'data': [],
            'errors': [e],
        }, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def asset_request_details_view(request, *args, **kwargs):

    try:
        qs = AssetRequest.objects.filter(pk=kwargs['pk'])[0]
        data = AssetRequestSerializer(qs, many=False).data
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
def asset_request_add_view(request, *args, **kwargs):

    serializer = AssetRequestSerializer(data=request.data)

    try:
        if serializer.is_valid(raise_exception=True):
            asset_name = serializer.validated_data.get('asset_name')
            serial_number = serializer.validated_data.get('serial_number')
            model = serializer.validated_data.get('model')
            company = serializer.validated_data.get('company')

            serializer.save(
                asset_name=asset_name, serial_number=serial_number, model=model, company=company)

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
