from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^logout/$', 'sunlightauth.views.logout', name='logout'),
)

