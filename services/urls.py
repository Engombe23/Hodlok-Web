from django.urls import path
from services import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import DigitalServiceSitemap, MarketingServiceSitemap

sitemaps = {
  'services': DigitalServiceSitemap,
  'services': MarketingServiceSitemap
}

urlpatterns = [
    path("", views.hodlok_services, name='services'),
    path("digital/", views.digital_services, name='digital'),
    path("marketing/", views.marketing_services, name='marketing'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemap}, name='django.contrib.sitemaps.views.sitemap'),
]