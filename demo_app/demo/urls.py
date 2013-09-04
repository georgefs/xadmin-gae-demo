from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
import xadmin
xadmin.autodiscover()

urlpatterns = patterns('',
   url(r'', include(xadmin.site.urls)),
)
