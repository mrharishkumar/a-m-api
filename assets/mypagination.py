from rest_framework.pagination import PageNumberPagination

class MyPagination(PageNumberPagination):
    default_limit=5
    limit_query_param='p'
    offset_query_param='data'
    max_limit=10
