from django.contrib.sitemaps import Sitemap
from .models import DigitalService, MarketingService

class DigitalServiceSitemap(Sitemap):
  changefreq = "weekly"
  priority = 0.8
  protocol = 'https'

  def items(self):
    return DigitalService.objects.all()
  
  def location(self):
    return 'services/digital'