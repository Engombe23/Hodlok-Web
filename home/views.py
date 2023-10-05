from django.shortcuts import render

from .models import Service

def home(request):
    main_solution = Service.objects.all()
    context = {"services": main_solution}
    return render(request, "home.html", context)

def privacy(request):
    return render(request, "privacy.html", {})