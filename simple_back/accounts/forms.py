from django import forms

from .models import CustomerProfile, ProviderProfile


class BaseProfileUpdateForm(forms.ModelForm):
    """
    Базовая форма обновления данных профиля
    """

    def __init__(self, *args, **kwargs):
        """
        Обновление стилей формы обновления
        """
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'autocomplete': 'off'
            })


class CustomerProfileUpdateForm(BaseProfileUpdateForm):
    """
    Форма обновления данных профиля заказчика
    """
    class Meta:
        model = CustomerProfile
        fields = ('name', 'contact_data', 'specialty', 'info')


class ProviderProfileUpdateForm(BaseProfileUpdateForm):
    """
    Форма обновления данных профиля исполнителя
    """
    class Meta:
        model = ProviderProfile
        fields = ('name', 'contact_data', 'specialty', 'info', 'experience_in_years')
