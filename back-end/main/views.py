from rest_framework.response import Response
from .serializers import WiredSerializer
from rest_framework import viewsets
from .models import Wired
from rest_framework.pagination import PageNumberPagination



class PostViewSet(viewsets.ViewSet, list):
  pagination_class = PageNumberPagination
  def create(self, request):
    try:
      data = request.data
      serializer = WiredSerializer(data=data)
      serializer.is_valid(raise_exception=True)
      serializer.save()
      print(serializer.data)
      return Response(data=serializer.data, status=200)
    except Exception as e:
      print(e)
      return Response({
          'error': str(e)
      }, status=400)
    
  def list(self, request):
    queryset = Wired.objects.all().order_by('-date_of_publish')
    paginator = PageNumberPagination()
    result_page = paginator.paginate_queryset(queryset, request)
    serializer = WiredSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)
