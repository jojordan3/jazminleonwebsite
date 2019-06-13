from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jup7!ka0b7n9fi@l22t^h^x_&qw#c!fxu(&vb(*i=mo+kqxmv#'

# Add your site's domain name(s) here.
ALLOWED_HOSTS = ['www.jazminleoncoaching.com']

# To send email from the server, we recommend django_sendmail_backend
# Or specify your own email backend such as an SMTP server.
# https://docs.djangoproject.com/en/2.1/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.google.com'
EMAIL_HOST_USER = DJANGO_ADMIN_EMAIL
EMAIL_HOST_PASSWORD = DJANGO_EMAIL_PASSWORD
EMAIL_PORT = 587

# Default email address used to send messages from the website.
DEFAULT_FROM_EMAIL = 'Jazmin Leon LLC <info@jazminleoncoaching.com>'

# A list of people who get error notifications.
ADMINS = [
    ('Jazmin Leon', 'jazmin.leon.llc@gmail.com'),
    ('Joanne Jordan', 'joanne.k.m.jordan@gmail.com'),
]

# A list in the same format as ADMINS that specifies who should get broken link
# (404) notifications when BrokenLinkEmailsMiddleware is enabled.
MANAGERS = ADMINS

# Email address used to send error messages to ADMINS.
SERVER_EMAIL = DEFAULT_FROM_EMAIL

# Use template caching to speed up wagtail admin and front-end.
# Requires reloading web server to pick up template changes.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'wagtail.contrib.settings.context_processors.settings',
            ],
            'loaders': [
                ('django.template.loaders.cached.Loader', [
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                ]),
            ],
        },
    },
]

CACHES = {
    'default': {
	'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
	'LOCATION': [
	    '127.0.0.1:11211',
    	]
    },
    'redis': {
	'BACKEND': 'django_redis.cache.RedisCache',
	'LOCATION': REDIS_CACHE_URL,
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
            'IGNORE_EXCEPTIONS': True,
        },
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}

DATABASES['default']['ATOMIC_REQUESTS'] = True  # noqa F405
DATABASES['default']['CONN_MAX_AGE'] = 60

try:
    from .local_settings import *
except ImportError:
    pass
