from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import AssetRequest, User
from .models import Status
from .serializers import AssetRequestSerializer
from assets.models import Asset
from assets.serializers import AssetSerializer
from django.template.loader import get_template
from django.core.mail import EmailMessage


# Create your views here.


@api_view(['GET'])
def asset_request_list_view(request, *args, **kwargs):

    try:
        qs = AssetRequest.objects.filter(employee_id=request.user.id)
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
        qs = AssetRequest.objects.get(pk=kwargs['pk'])

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

    request.data['employee_id'] = request.user.id
    serializer = AssetRequestSerializer(data=request.data)

    try:
        if serializer.is_valid(raise_exception=True):

            asset_id = serializer.validated_data.get('asset_id')
            employee_id = serializer.validated_data.get('employee_id')
            remarks = serializer.validated_data.get('remarks')
            asset = Asset.objects.filter(pk=request.data['asset_id'])[0]
            get_email = User.objects.filter(username=employee_id).values()
            asset_data = AssetSerializer(asset).data
            for i in get_email:
                email = i['email']
                new = {'email': email}
                asset_data.update(new)
                message = get_template("email.html").render(asset_data)
                mail = EmailMessage(subject=f'Request For Asset By {email}', body=message, from_email='rahul.katoch@impressico.com', to=[
                                    'rahulkatoch99@gmail.com', 'harish.kumar@impressico.com'])
                mail.content_subtype = "html"
                mail.mixed_subtype = 'related'
                mail.send()
            sta = asset_data['status']
            if sta == 'AVAILABLE':
                asset_data['status'] = "UNAVAILABLE"
                asset_serialize = AssetSerializer(
                    instance=asset, data=asset_data)
                if asset_serialize.is_valid(raise_exception=True):
                    asset_serialize.save()

                serializer.save(
                    asset_id=asset_id, employee_id=employee_id, remarks=remarks)

                return Response({
                    'data': [serializer.data],
                    'errors': [],
                }, status=status.HTTP_200_OK)
            else:
                return Response({
                    'data': [],
                    'errors': ['Device Unavailable']
                })

    except Exception as e:
        e = str(e)

        return Response({
            'data': [],
            'errors': [e],
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['DELETE'])
def asset_request_remove_view(request, *args, **kwargs):

    try:
        qs = AssetRequest.objects.get(pk=kwargs['pk'])
        data = AssetRequestSerializer(qs).data

        if request.user.is_superuser:
            asset = Asset.objects.filter(pk=data['asset_id'])[0]

            asset_data = AssetSerializer(asset).data

            # sta= asset_data['status']
            asset_data['status'] = "AVAILABLE"
            asset_serialize = AssetSerializer(instance=asset, data=asset_data)
            if asset_serialize.is_valid(raise_exception=True):
                asset_serialize.save()
            qs.delete()
            return Response({
                'data': [],
                'errors': [],
            }, status=status.HTTP_200_OK)

        if data['status'] == Status.PENDING and \
                request.user.id == data['employee_id']:
            asset = Asset.objects.filter(pk=data['asset_id'])[0]

            asset_data = AssetSerializer(asset).data

            # sta= asset_data['status']
            asset_data['status'] = "AVAILABLE"
            asset_serialize = AssetSerializer(instance=asset, data=asset_data)
            if asset_serialize.is_valid(raise_exception=True):
                asset_serialize.save()
            qs.delete()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response({"error": "Not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    except Exception as e:
        e = str(e)
        return Response({
            'data': [],
            'errors': [e]
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
def asset_update_Status(request, *args, **kwargs):
    qs = AssetRequest.objects.get(pk=kwargs['pk'])
    try:
        data = AssetRequestSerializer(qs).data

        asset = Asset.objects.filter(pk=data['asset_id'])[0]

        asset_data = AssetSerializer(asset).data

        asset_status = data['status']
        if asset_status == "DENIED" or asset_status == "RETURNED":
            asset_data['status'] = "AVAILABLE"
            asset_serialize = AssetSerializer(instance=asset, data=asset_data)
            if asset_serialize.is_valid(raise_exception=True):
                asset_serialize.save()
        return Response({
            'data': [data],
            'errors': [],
        }, status=status.HTTP_200_OK)
    except Exception as e:
        e = str(e)
        return Response({
            'data': [],
            'errors': [e]
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
