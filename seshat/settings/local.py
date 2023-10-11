# flake8: noqa

from .base import *

#INSTALLED_APPS += ["debug_toolbar"]

#MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")
#MIDDLEWARE.insert(0, "debug_toolbar.middleware.DebugToolbarMiddleware")


# Databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'seshat_oct5',
        'USER': 'postgres',
        # 'PASSWORD': config('DB_PASSWORD'),
        'HOST': 'localhost',
        'PORT': 5432,
    }
}

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
