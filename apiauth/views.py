from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from django.contrib.auth.models import User

# Create your views here.


@api_view(['GET'])
def getusername(request):
    try:
        user = User.objects.get(pk=request.user.id)
        data = {'username': f'{user.first_name} {user.last_name}'}
        return Response({
            'data': [data],
            'errors': []
        }, status=status.HTTP_200_OK)
    except Exception as e:
        e = str(e)
        return Response({
            'data': [],
            'errors': [e]
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
