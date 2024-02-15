# flake8: noqa

from .base import *
import environ
import os
import sys

#MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")
#MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")

# Databases
# We use the local database for development and the GitHub Actions database for testing
if os.getenv('GITHUB_ACTIONS') == 'true':
    DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': 'github_actions',
            'USER': 'postgres',
            'HOST': 'postgres',
            'PORT': '5432',
            'PASSWORD': 'postgres'
        }
    }
else:

    # Initialise environment variables
    env = environ.Env()
    environ.Env.read_env()

    DATABASES = {
        'default': {
            'ENGINE': 'django.contrib.gis.db.backends.postgis',
            'NAME': env('NAME'),
            'USER': 'postgres',
            'HOST': env('HOST'),
            'PORT': env('PORT'),
            'PASSWORD': env('PASSWORD')
        }
    }

# Shapefile spatial stuff
GEOGRAPHIC_DB = True

if sys.platform.startswith('darwin'): # macOS
    GDAL_LIBRARY_PATH = '/opt/homebrew/opt/gdal/lib/libgdal.dylib'
    GEOS_LIBRARY_PATH = '/opt/homebrew/opt/geos/lib/libgeos_c.dylib'
else: # linux
    GDAL_LIBRARY_PATH = '/usr/lib/libgdal.so'
    if os.getenv('GITHUB_ACTIONS') == 'true':
        GEOS_LIBRARY_PATH = '/usr/lib/x86_64-linux-gnu/libgeos_c.so'
    else:
        GEOS_LIBRARY_PATH = '/usr/lib/aarch64-linux-gnu/libgeos_c.so'

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

ALLOWED_HOSTS = ['127.0.0.1',
                 'localhost',
                 '20.68.162.158']

if 'test' in sys.argv:
    STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'