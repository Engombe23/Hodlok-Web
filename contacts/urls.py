from django.urls import path
from contacts import views
from django.contrib.sitemaps.views import sitemap
from .sitemaps import StaticViewSitemap

sitemaps = {
  'static':StaticViewSitemap
}

urlpatterns = [
    path('', views.contact, name='contacts'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('sitemap.xml', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
]
