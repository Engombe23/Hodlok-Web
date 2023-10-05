from django.shortcuts import render

from .models import DigitalService, MarketingService
from home.models import Service

def hodlok_services(request):
    services = Service.objects.all()
    context = {'services' : services}
    return render(request, "services.html", context)

def digital_services(request):
    digitalServices = DigitalService.objects.all()
    context = {'digital_services': digitalServices}
    return render(request, 'digital.html', context)

def marketing_services(request):
    marketingServices = MarketingService.objects.all()
    context = {'marketing_services': marketingServices}
    return render(request, 'marketing.html', context)