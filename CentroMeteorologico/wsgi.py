"""
WSGI config for CentroMeteorologico project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import sys

from django.contrib.staticfiles.handlers import StaticFilesHandler
from django.core.wsgi import get_wsgi_application

path = os.path.expanduser('~/django_projects/CentroMeteorologico')
if path not in sys.path:
    sys.path.insert(0, path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CentroMeteorologico.settings')

application = StaticFilesHandler(get_wsgi_application())
