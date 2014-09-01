from django.conf.urls import patterns, include, url
from django.contrib import admin
import Notes.urls


admin.autodiscover()

urlpatterns = patterns('',
    url(r'^notes/', include(Notes.urls)),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'^oauth2/', include('provider.oauth2.urls', namespace='oauth2')),
)
