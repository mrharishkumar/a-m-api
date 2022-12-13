from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Branch
from .serializers import BranchSerializer

# Create your views here.


@api_view(['GET'])
def branch_list_view(request, *args, **kwargs):

    try:
        qs = Branch.objects.all()
        data = BranchSerializer(qs, many=True).data

        return Response({
            'data': data,
            'errors': [],
        }, status=status.HTTP_200_OK)

    except Exception as e:
        e = str(e)

        return Response({
            'data': [],
            'errors': [e],
        }, status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def brach_details_view(request, *args, **kwargs):

    try:
        qs = Branch.objects.filter(pk=kwargs['pk'])[0]
        data = BranchSerializer(qs).data

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
def add_branch_view(request, *args, **kwargs):

    serializer = BranchSerializer(data=request.data)

    try:
        if serializer.is_valid(raise_exception=True):
            branch_name = serializer.validated_data.get('branch')

            serializer.save(branch_name=branch_name)

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
