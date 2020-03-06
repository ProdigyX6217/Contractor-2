"""
WSGI config for yohancescorner project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

import dotenv
from django.core.wsgi import get_wsgi_application

dotenv.read_dotenv('.env')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yohancescorner.settings')

application = get_wsgi_application()
