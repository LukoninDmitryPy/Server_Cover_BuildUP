from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import FileViewSet


v1_router = DefaultRouter()
v1_router.register('files', FileViewSet, basename='files')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]
