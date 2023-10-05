from django.urls import path
from services import views

urlpatterns = [
    path("", views.hodlok_services, name='services'),
    path("digital/", views.digital_services, name='digital'),
    path("marketing/", views.marketing_services, name='marketing'),
]