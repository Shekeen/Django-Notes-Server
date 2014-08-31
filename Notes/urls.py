from django.conf.urls import patterns, url, include
from rest_framework import urls as rf_urls
from .views import NoteList, NoteDetail


urlpatterns = patterns('',
    url(r'^$', NoteList.as_view()),
    url(r'^(?P<pk>\d+)/$', NoteDetail.as_view()),

    url(r'^oauth2/', include('provider.oauth2.urls', namespace='oauth2')),
)

urlpatterns += rf_urls.urlpatterns
