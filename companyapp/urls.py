from django.conf.urls import include, url
from . import views
from django.contrib.sitemaps.views import sitemap
from .sitemap import PostSitemap
sitemaps = {
    'pages': PostSitemap
}
urlpatterns = [
    url(r'^$', views.home,name ="home"),
    url(r'^quality/$', views.quality, name='quality'),
    url(r'^cleaning/$', views.cleaning, name='cleaning'),
    url(r'^propertyservice/$', views.propertyservice, name='propertyservice'),
    url(r'^kategori/(?P<title>[^/]+)/$', views.pages,name ="pages"),
    url(r'^sitemap\.xml/$', sitemap, {'sitemaps': sitemaps}, name='sitemap'),




]
