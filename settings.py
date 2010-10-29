# Django settings for thefoundation project.
import os
PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Jeremy Carbaugh', 'jcarbaugh@sunlightfoundation.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'thefoundation.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute path to the directory that holds media.
# Example: "/home/media/media.lawrence.com/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, 'static')

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash if there is a path component (optional in other cases).
# Examples: "http://media.lawrence.com", "http://example.com/media/"
MEDIA_URL = '/static/'

# URL prefix for admin media -- CSS, JavaScript and images. Make sure to use a
# trailing slash.
# Examples: "http://foo.com/media/", "/media/".
ADMIN_MEDIA_PREFIX = 'http://assets.sunlightfoundation.com/admin/1.2.3/'

# Make this unique, and don't share it with anybody.
SECRET_KEY = '***REMOVED***'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware',
)

ROOT_URLCONF = 'thefoundation.urls'

TEMPLATE_DIRS = (
    os.path.join(PROJECT_ROOT, 'templates'),
)

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.flatpages',
    'django.contrib.markup',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'debug_toolbar',
    'mediasync',
    'sunlightfoundation.presscenter',
    'sunlightfoundation.policy',
    'sunlightfoundation.spammer',
    'sunlightfoundation.com',
    'sunlightfoundation.donations',
    'sunlightfoundation.earmarkdisclosures',
    'sunlightfoundation.fortune535',
    'sunlightfoundation.signups',
    'gunicorn',
)

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

AUTH_PROFILE_MODULE = "com.UserProfile"
AUTHENTICATION_BACKENDS = (
    'googleauth.backends.GoogleAuthBackend',
    'django.contrib.auth.backends.ModelBackend',
)

GOOGLEAUTH_IS_STAFF = True
GOOGLEAUTH_DOMAIN = 'sunlightfoundation.com'
#GOOGLEAUTH_REALM = 'should be set using the Sites framework'

INTERNAL_IPS = ('127.0.0.1',)
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

MEDIASYNC = {
    'BACKEND': 'mediasync.backends.s3',
    'AWS_KEY': '***REMOVED***',
    'AWS_SECRET': '***REMOVED***',
    'AWS_BUCKET': 'assets.sunlightfoundation.com',
    'AWS_PREFIX': 'site/4.0',
    'AWS_BUCKET_CNAME': True,
    'DOCTYPE': 'html5',
    'CACHE_BUSTER': 1234567890,
    'JOINED': {
        'styles/thefoundation.css': (
            'styles/style.css',
            'styles/handheld.css',
            'styles/screen.css',
        ),
        'scripts/thefoundation.js': (
            'scripts/jquery.jcarousel.min.js',
            'scripts/jquery.placehold-0.3.min.js',
            'scripts/plugins.js',
            'scripts/script.js',
        ),
    },
}

HAYSTACK_SITECONF = 'sunlightfoundation.com.search_sites'
HAYSTACK_SEARCH_ENGINE = 'whoosh'
HAYSTACK_WHOOSH_PATH = os.path.join(PROJECT_ROOT, 'whoosh.index')

SF_PRESSRELEASE_LIFETIME = 14

MAILINGLIST_SUBSCRIBED_URL = "/join/thankyou/"
MAILINGLIST_REQUIRED_FIELDS = {
    "email": u"A valid email address is required",
}

CONTACT_FORM_RECIPIENTS = ['contact@sunlightfoundation.com',]
GRANT_APPLICATION_RECIPIENTS = ['swells@sunlightfoundation.com','jcarbaugh@sunlightfoundation.com','habdullah@sunlightfoundation.com']

SIGNUPS_FROM_EMAIL = 'contact@sunlightfoundation.com'

try:
    from local_settings import *
except ImportError:
    pass