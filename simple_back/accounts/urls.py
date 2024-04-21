from django.contrib import admin
from django.urls import path

from . import views

app_name = 'accounts'


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.IndexView.as_view(), name='home'),
    path('provider/', views.ProviderView.as_view(), name='provider'),
    path('provider/update', views.ProviderProfileUpdateView.as_view(), name='provider_update'),
    path('customer/', views.CustomerView.as_view(), name='customer'),
    path('customer/update', views.CustomerProfileUpdateView.as_view(), name='customer_update'),
]