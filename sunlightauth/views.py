from django.contrib.auth import logout as auth_logout
from django.http import HttpResponseRedirect
from django.utils.http import is_safe_url
from social_auth.utils import setting

def logout(request):
    """ log user out and redirect them to a next page or site root """
    auth_logout(request)

    redirect_to = request.REQUEST.get('next', '')

    if redirect_to:
        if not is_safe_url(url=next_page, host=request.get_host()):
            next_page = request.path
    if not next_page:
        next_page = '/'

    ## prepend host (use sites framework?)
    next_page = '' + next_page

    logout_url = ''.join(
        setting('SUNLIGHT_AUTH_BASE_URL',
                'http://login.sunlightfoundation.com/'),
        'accounts/logout/',
    )
    return HttpResponseRedirect(logout_url)
