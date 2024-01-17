"""
ASGI config for seshat project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os
from pathlib import Path

from django.core.asgi import get_asgi_application

local_env_path = str(Path.cwd()) + "/seshat/settings/.env"
if os.path.exists(local_env_path):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                            'seshat.settings.local')
else:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                            'seshat.settings.production')

application = get_asgi_application()
