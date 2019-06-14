from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jup7!ka0b7n9fi@l22t^h^x_&qw#c!fxu(&vb(*i=mo+kqxmv#'

ALLOWED_HOSTS = ['*']

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.google.com'
EMAIL_PORT = 587

WAGTAIL_CACHE = False

#try:
#    from .local_settings import *
#except ImportError:
#    pass
