from django.contrib import admin

from .models import CustomerProfile, ProviderProfile

EMPTY_VALUE = 'нет информации'


@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_data', 'specialty', 'info')
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = EMPTY_VALUE


@admin.register(ProviderProfile)
class CustomerProfileAdmin(admin.ModelAdmin):
    list_display = ('name', 'contact_data', 'specialty', 'info', 'experience_in_years')
    search_fields = ('name',)
    list_filter = ('name',)
    empty_value_display = EMPTY_VALUE