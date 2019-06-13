"""
WSGI config for jlcoaching project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

from django.core.management import execute_from_command_line
execute_from_command_line('wagtail updatemodulepaths')

from django.core.wsgi import get_wsgi_application

#os.environ.setdefault("DJANGO_SETTINGS_MODULE", "jlcoaching.settings.dev")

application = get_wsgi_application()
