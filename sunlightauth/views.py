from django.contrib.auth import logout as auth_logout
from django.contrib.sites.models import Site
from django.http import HttpResponseRedirect
from django.utils.http import is_safe_url
from django.conf import settings

def logout(request):
    """ log user out and redirect them to a next page or site root """
    auth_logout(request)

    redirect_to = request.REQUEST.get('next', '')

    # validate that we're using a safe url
    if redirect_to:
        if not is_safe_url(url=redirect_to, host=request.get_host()):
            redirect_to = request.path

    # if it still isn't set, return to /
    if not redirect_to:
        redirect_to = '/'

    ## prepend host (use sites framework?)
    redirect_to = 'http://' + Site.objects.get_current().domain + redirect_to

    BASE = 'https://login.sunlightfoundation.com/'
    if hasattr(settings, 'SUNLIGHT_AUTH_BASE_URL'):
        BASE = settings.SUNLIGHT_AUTH_BASE_URL

    logout_url = ''.join((settings.SUNLIGHT_AUTH_BASE_URL,
                          'accounts/logout/?next=',
                          redirect_to))

    return HttpResponseRedirect(logout_url)
