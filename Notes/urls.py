from django.conf.urls import patterns, url
from Notes.views import NoteList, NoteDetail


urlpatterns = patterns('',
    url(r'^$', NoteList.as_view()),
    url(r'^(?P<pk>\d+)/$', NoteDetail.as_view()),
)
