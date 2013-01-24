Provides an authentication backend that works in conjunction w/ Django and
django-social-auth to allow logging in via the login.sunlightfoundation.com
backend.

Requires a client key/secret pair from login.sunlightfoundation.com. If you
are looking at this from outside of Sunlight it probably isn't very useful 
(perhaps just to serve as a very basic example of how to write a 
django-social-auth backend)

Installation
============
Add 'social_auth' to INSTALLED_APPS if it isn't already

Also add auth URLS:
    url(r'', include('sunlightauth.urls')),

Add 'sunlightauth.backends.SunlightBackend' to AUTHENTICATION_BACKENDS
)

Also set the following settings:

SUNLIGHT_AUTH_BASE_URL
    Base URL (defaults to 'http://login.sunlightfoundation.com', only change
              for testing)
              
SUNLIGHT_AUTH_APP_ID
    OAuth2 client app id
    
SUNLIGHT_AUTH_SECRET
    OAuth2 client secret
    
SUNLIGHT_AUTH_SCOPE
    generally is set to []
