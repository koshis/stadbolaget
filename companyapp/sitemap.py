from django.contrib.sitemaps import Sitemap
from .models import MenuItem,Menucategory
 
 
class PostSitemap(Sitemap):    
    changefreq = "monthly"
    priority = 0.9
 
    def items(self):
        return Menucategory.objects.all()
 
    # def lastmod(self, obj):
    #     return Pages.published
