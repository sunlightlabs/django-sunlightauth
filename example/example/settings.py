DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'example.db',
    }
}

TIME_ZONE = 'America/New_York'

MEDIA_ROOT = ''
MEDIA_URL = ''
STATIC_ROOT = ''
STATIC_URL = '/static/'
SECRET_KEY = 'nm!ejfr(-(3nsl+84@m%(m1_wsijwj14855^280qp*-=0g-dv-'
ROOT_URLCONF = 'example.urls'
WSGI_APPLICATION = 'example.wsgi.application'

TEMPLATE_DIRS = (
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'social.apps.django_app.default',
)

AUTHENTICATION_BACKENDS = (
    'sunlightauth.backends.SunlightBackend',
)

# SUNLIGHT_AUTH_BASE_URL = 'http://localhost:8000/'
SOCIAL_AUTH_SUNLIGHT_KEY = 'a-id'
SOCIAL_AUTH_SUNLIGHT_SECRET = 'a-secret'


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
