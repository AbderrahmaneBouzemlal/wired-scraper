from django.urls import path
from .views import PostViewSet

urlpatterns = [
    path('', PostViewSet.as_view({'get': 'list'}), name="read_data"),
    path('create', PostViewSet.as_view({'post': 'create'}), name="post_data_from_scrappe"),
]
