"""
WSGI config for blog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/howto/deployment/wsgi/
"""

import os

# from django.core.wsgi import get_wsgi_application
#
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'blog.settings')
#
# application = get_wsgi_application()

from django.core.wsgi import get_wsgi_application

if os.environ.get('DEV') is True:
   os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blog.settings.dev")
else:
   os.environ.setdefault("DJANGO_SETTINGS_MODULE",
   "blog.settings.production")

application = get_wsgi_application()
