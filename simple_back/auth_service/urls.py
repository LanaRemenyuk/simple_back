from django.urls import include, path
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from .views import CustomUserViewSet

app_name = 'auth'

router = routers.DefaultRouter()
router_v1 = DefaultRouter()
router_v1.register('auth', CustomUserViewSet, basename='auth')


urlpatterns = [
    path('', include(router_v1.urls)),
    path('', include('djoser.urls')),
    path('', include('djoser.urls.jwt')),
]