from django.conf.urls import patterns, url, include

urlpatterns = patterns(
    '',
    url(r'^logout/$', 'sunlightauth.views.logout', name='logout'),
    url('', include('social.apps.django_app.urls', namespace='social'))
)

