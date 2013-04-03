from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()


urlpatterns = patterns('',
    url(r'^admin/mobile/', include('mobileadmin.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
