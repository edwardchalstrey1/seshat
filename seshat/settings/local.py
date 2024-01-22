# flake8: noqa

from .base import *
import environ
# Initialise environment variables
env = environ.Env()
environ.Env.read_env()

INSTALLED_APPS = [
    "seshat.apps.accounts",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",

    'django.contrib.sites', # Add this


    'django.contrib.humanize',
    'crispy_forms',
    "seshat.apps.core",
    "seshat.apps.general",
    "seshat.apps.sc",
    "seshat.apps.wf",
    "seshat.apps.crisisdb",
    "seshat.apps.seshat_api",
    "django_filters",
    "corsheaders",
    "rest_framework",
    "mathfilters",
    # all-auth
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    #'allauth.socialaccount.providers.github',
    'allauth.socialaccount.providers.google',
    'django.contrib.gis',
    'leaflet',

]

#MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")
#MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")


# Databases
DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': env('NAME'),
        'USER': env('USER'),
        'HOST': env('HOST'),
        'PORT': env('PORT')
    }
}

# Shapefile spatial stuff
GEOGRAPHIC_DB = True

# TODO: Find a way to not hardcode:
GDAL_LIBRARY_PATH = '/opt/homebrew/opt/gdal/lib/libgdal.dylib'
GEOS_LIBRARY_PATH = '/opt/homebrew/opt/geos/lib/libgeos_c.dylib'

django_settings_module = os.environ.get('DJANGO_SETTINGS_MODULE')

#print("###################",django_settings_module)
#print(DATABASES)

my_current_server = "127.0.0.1:8000"
# ==============================================================================
# EMAIL SETTINGS
# ==============================================================================

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
######EMAIL_CONFIRMATION_BRANCH is the keyword that needs to be searched
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'