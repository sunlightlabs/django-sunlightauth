""" Sunlight OAuth support.  """
try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

import json
from social.backends.oauth import BaseOAuth2

from django.conf import settings


BASE_SUNLIGHT_URL = 'https://login.sunlightfoundation.com/'
if hasattr(settings, 'SUNLIGHT_AUTH_BASE_URL'):
    BASE_SUNLIGHT_URL = settings.SUNLIGHT_AUTH_BASE_URL

SUNLIGHT_AUTHORIZATION_URL = '%soauth2/authorize/' % BASE_SUNLIGHT_URL
SUNLIGHT_ACCESS_TOKEN_URL = '%soauth2/token/' % BASE_SUNLIGHT_URL
SUNLIGHT_USER_DATA_URL = '%sapi/userinfo/' % BASE_SUNLIGHT_URL


class SunlightBackend(BaseOAuth2):
    """Sunlight OAuth authentication backend"""
    AUTHORIZATION_URL = SUNLIGHT_AUTHORIZATION_URL
    ACCESS_TOKEN_URL = SUNLIGHT_ACCESS_TOKEN_URL
    ACCESS_TOKEN_METHOD = 'POST'
    REDIRECT_STATE = False
    ID_KEY = 'email'

    name = 'sunlight'

    def user_data(self, access_token, *args, **kwargs):
        """Loads user data from service"""
        return self.get_json(
            SUNLIGHT_USER_DATA_URL,
            params={'access_token': access_token},
        )

    def get_user_details(self, response):
        """Return user details from Sunlight login server"""
        return {'username': response.get('username'),
                'email': response.get('email'),
                'first_name': response.get('first_name'),
                'last_name': response.get('last_name'),
                'is_staff': response.get('is_staff'),
                'is_superuser': response.get('is_superuser'),
               }
