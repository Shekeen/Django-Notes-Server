from django.conf.urls import patterns, include, url
from django.contrib import admin
from Notes.views import UserList, UserDetail
import Notes.urls


urlpatterns = patterns('',
    url(r'^notes/', include(Notes.urls)),
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('',
    url(r'^users/$', UserList.as_view()),
    url(r'^users/(?P<pk>\d+)/$', UserDetail.as_view()),
)

urlpatterns += patterns('',
    url(r'^auth/', include('rest_framework.urls', namespace='rest_framework')),
)