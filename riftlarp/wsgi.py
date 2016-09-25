"""
WSGI config for riftlarp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
os.system("echo 'belk' > /tmp/belk")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "riftlarp.settings")

application = get_wsgi_application()
