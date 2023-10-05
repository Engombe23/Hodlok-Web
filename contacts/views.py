from django.shortcuts import render

def contact(request):
    return render(request, "contacts.html", {})

def thankyou(request):
    return render(request, "thankyou.html", {})