from django.contrib.sitemaps import Sitemap
from .models import Pages
 
 
class PostSitemap(Sitemap):    
    changefreq = "monthly"
    priority = 0.9
 
    def items(self):
        return Pages.objects.all()
 
    # def lastmod(self, obj):
    #     return Pages.published
