from django.conf.urls import patterns, include, url
from django.contrib import admin
import Notes.urls


urlpatterns = patterns('',
    url(r'^notes/', include(Notes.urls)),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'^oauth2/', include('oauth2_provider.urls', namespace='oauth2_provider')),
)
