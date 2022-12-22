from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Asset
from .serializers import AssetSerializer
from .models import AssetStatus


# Create your views here.


@api_view(['GET'])
def asset_list_view(request, *args, **kwargs):

    try:
        qs = Asset.objects.filter(status=AssetStatus.AVAILABLE)
        data = AssetSerializer(qs, many=True).data
        # page=Paginator(data,4)
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
def asset_details_view(request, *args, **kwargs):

    try:
        qs = Asset.objects.get(pk=kwargs['pk'])
        print("qs", qs)
        data = AssetSerializer(qs).data
        print("data", data)
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
def asset_add_view(request, *args, **kwargs):

    serializer = AssetSerializer(data=request.data)

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

