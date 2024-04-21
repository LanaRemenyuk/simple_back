from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, render
from django.views import View
from .forms import ProviderProfileUpdateForm, CustomerProfileUpdateForm
from .models import CustomerProfile, ProviderProfile
from django.http import HttpResponseRedirect
from django.urls import reverse


class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class ProviderView(View):
    def get(self, request):
        try:
            provider = ProviderProfile.objects.get(id=request.user.id)
        except ProviderProfile.DoesNotExist:
            provider = None

        data = {'provider': provider}
        return render(request, 'provider.html', data)


class ProviderProfileUpdateView(LoginRequiredMixin, View):
    def get(self, request):
        provider = get_object_or_404(ProviderProfile, id=request.user.id)
        form = ProviderProfileUpdateForm(instance=provider)
        context = {
            'form': form
        }
        return render(request, 'provider_edit.html', context)

    def post(self, request):
        provider = get_object_or_404(ProviderProfile, id=request.user.id)
        form = ProviderProfileUpdateForm(request.POST, instance=provider)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('accounts:provider'))
        context = {
            'form': form,
        }
        return render(request, 'provider.html', context)


class CustomerView(View):
    def get(self, request):
        try:
            customer = CustomerProfile.objects.get(id=request.user.id)
        except CustomerProfile.DoesNotExist:
            customer = None

        data = {'customer': customer}
        return render(request, 'customer.html', data)


class ProviderProfileUpdateView(LoginRequiredMixin, View):
    def get(self, request):
        provider, created = ProviderProfile.objects.get_or_create(id=request.user.id)
        form = ProviderProfileUpdateForm(instance=provider)
        context = {
            'form': form
        }
        return render(request, 'provider_edit.html', context)

    def post(self, request):
        provider, created = ProviderProfile.objects.get_or_create(id=request.user.id)
        form = ProviderProfileUpdateForm(request.POST, instance=provider)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('accounts:provider'))
        context = {
            'form': form,
        }
        return render(request, 'provider.html', context)


class CustomerProfileUpdateView(LoginRequiredMixin, View):
    def get(self, request):
        customer, created = CustomerProfile.objects.get_or_create(id=request.user.id)
        form = CustomerProfileUpdateForm(instance=customer)
        context = {
            'form': form
        }
        return render(request, 'customer_edit.html', context)

    def post(self, request):
        customer, created = CustomerProfile.objects.get_or_create(id=request.user.id)
        form = CustomerProfileUpdateForm(request.POST, instance=customer)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('accounts:customer'))
        context = {
            'form': form,
        }
        return render(request, 'customer.html', context)