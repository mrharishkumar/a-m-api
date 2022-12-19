from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import AssetRequest
from .models import Status
from .serializers import AssetRequestSerializer
from assets.models import Asset, AssetStatus
from assets.serializers import AssetSerializer
from django.core.mail import send_mail
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
            # verify = AssetRequest.objects.filter(asset_id=asset)                        # CHeck the data is already present or not
            # if verify:
            #     return Response({
            #         "data":[],
            #         "error":"The Request Is Already Presented"
            #     })
            asset_data = AssetSerializer(asset).data
            message=get_template("email.html").render(asset_data)
            mail = EmailMessage(subject="Request For Asset",body=message,from_email='rahul.katoch@impressico.com',to=['rahulkatoch99@gmail.com','harish.kumar@impressico.com'])
            mail.content_subtype = "html"
            mail.mixed_subtype = 'related'
            mail.send()
            sta= asset_data['status']
            print("sta",sta)
            if sta == 'AVAILABLE':
                asset_data['status']="UNAVAILABLE"
                asset_serialize = AssetSerializer(instance=asset,data=asset_data)
                if asset_serialize.is_valid(raise_exception=True):
                    asset_serialize.save()
            serializer.save(
                asset_id=asset_id, employee_id=employee_id, remarks=remarks)
            
            # default_status= serializer.data["status"]
            # print(default_status)
            # if default_status == "DENIED":
            #     asset_data['status']="AVAILABLE"
            #     asset_serialize = AssetSerializer(instance=asset,data=asset_data)
            #     if asset_serialize.is_valid(raise_exception=True):
            #         asset_serialize.save()
                
            # if default_status == "DENIED":
                
            # print("serializer data:",default_status)
            return Response({
                'data': [serializer.data],
                'errors': [],
            }, status=status.HTTP_200_OK)
            

    except Exception as e:
        e = str(e)
        print(e)

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
            qs.delete()
            return Response({
                'data': [],
                'errors': [],
            }, status=status.HTTP_200_OK)

        if data['status'] == Status.PENDING and \
                request.user.id == data['employee_id']:
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
