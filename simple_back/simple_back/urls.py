from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.contrib import admin
from django.urls import re_path as url
from django.urls import include, path
from rest_framework import permissions

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('auth_service.urls')),
    path('', include('accounts.urls'))
]

schema_view = get_schema_view(
   openapi.Info(
      title="Auth_service API",
      default_version='v1',
      description="Документация для приложения simple_back",
      contact=openapi.Contact(email="lan2828@yandex.ru"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
   url(r'^swagger(?P<format>\.json|\.yaml)$',
       schema_view.without_ui(cache_timeout=0), name='schema-json'),
   url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0),
       name='schema-swagger-ui'),
   url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0),
       name='schema-redoc'),
]
