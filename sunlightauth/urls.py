from django.conf.urls import patterns, url, include

urlpatterns = patterns(
    '',
    url(r'^logout/$', 'sunlightauth.views.logout', name='logout'),
    url(r'', include('social_auth.urls')),
)

