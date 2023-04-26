"""
WSGI config for wf_website project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from whitenoise import WhiteNoise

STATIC_URL = '/staticfiles/'


PROJECT_DIR = os.path.dirname(os.path.abspath(__file__))

BASE_DIR = os.path.dirname(PROJECT_DIR)

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.dev")
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

application = get_wsgi_application()
application = WhiteNoise(application, root=STATIC_ROOT)
application.add_files(STATIC_ROOT, prefix=STATIC_URL)
