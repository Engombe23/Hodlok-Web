from django.contrib.sitemaps import Sitemap
from django.urls import reverse

class StaticViewSitemap(Sitemap):
  changefreq = "daily"
  priority = 0.8
  protocol = 'https'

  def items(self):
    return ['home','services','contacts']
  
  def location(self, item):
    return reverse(item)