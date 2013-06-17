""" Sunlight OAuth support.  """
from urllib import urlencode
import json
from social_auth.utils import setting, dsa_urlopen
from social_auth.backends import BaseOAuth2, OAuthBackend


BASE_SUNLIGHT_URL = setting('SUNLIGHT_AUTH_BASE_URL',
                            'https://login.sunlightfoundation.com/')
SUNLIGHT_AUTHORIZATION_URL = '%soauth2/authorize/' % BASE_SUNLIGHT_URL
SUNLIGHT_ACCESS_TOKEN_URL = '%soauth2/token/' % BASE_SUNLIGHT_URL
SUNLIGHT_USER_DATA_URL = '%sapi/userinfo/' % BASE_SUNLIGHT_URL


class SunlightBackend(OAuthBackend):
    """Sunlight OAuth authentication backend"""
    name = 'sunlight'

    # use this key as a globally unique user id
    ID_KEY = 'email'

    def get_user_details(self, response):
        """Return user details from Sunlight login server"""
        return {'username': response.get('username'),
                'email': response.get('email'),
                'first_name': response.get('first_name'),
                'last_name': response.get('last_name'),
                'is_staff': response.get('is_staff'),
                'is_superuser': response.get('is_superuser'),
               }


class SunlightAuth(BaseOAuth2):
    """Sunlight OAuth2 mechanism"""
    AUTHORIZATION_URL = SUNLIGHT_AUTHORIZATION_URL
    ACCESS_TOKEN_URL = SUNLIGHT_ACCESS_TOKEN_URL
    AUTH_BACKEND = SunlightBackend
    SETTINGS_KEY_NAME = 'SUNLIGHT_AUTH_APP_ID'
    SETTINGS_SECRET_NAME = 'SUNLIGHT_AUTH_SECRET'
    SCOPE_VAR_NAME = 'SUNLIGHT_AUTH_SCOPE'
    SCOPE_SEPARATOR = ','
    REDIRECT_STATE = False

    def user_data(self, access_token, *args, **kwargs):
        """Loads user data from service"""
        url = SUNLIGHT_USER_DATA_URL + '?' + urlencode({
            'access_token': access_token
        })
        try:
            return json.load(dsa_urlopen(url))
        except ValueError:
            return None


# expose backend to django-social-auth
BACKENDS = {'sunlight': SunlightAuth}
