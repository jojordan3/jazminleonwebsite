from .base import *
import django_heroku
import dj_database_url

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

# Add your site's domain name(s) here.
ALLOWED_HOSTS = ['www.jazminleon.com', 'www.jazminleoncoaching.com']

# To send email from the server, we recommend django_sendmail_backend
# Or specify your own email backend such as an SMTP server.
# https://docs.djangoproject.com/en/2.1/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.google.com'
EMAIL_HOST_USER = os.environ['DJANGO_ADMIN_EMAIL']
EMAIL_HOST_PASSWORD = os.environ['DJANGO_EMAIL_PASSWORD']
EMAIL_PORT = 587

# Default email address used to send messages from the website.
DEFAULT_FROM_EMAIL = 'Jazmin Leon LLC <noreply@jazminleon.com>'

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

SESSION_ENGINE = 'django.contrib.sessions.backends.cache'

servers = os.environ['MEMCACHIER_SERVERS']
username = os.environ['MEMCACHIER_USERNAME']
password = os.environ['MEMCACHIER_PASSWORD']

CACHES = {
    'default': {
        # Use pylibmc
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',

        # TIMEOUT is not the connection timeout! It's the default expiration
        # timeout that should be applied to keys! Setting it to `None`
        # disables expiration.
        'TIMEOUT': None,

        'LOCATION': servers,

        'OPTIONS': {
            # Use binary memcache protocol (needed for authentication)
            'binary': True,
            'username': username,
            'password': password,
            'behaviors': {
                # Enable faster IO
                'no_block': True,
                'tcp_nodelay': True,

                # Keep connection alive
                'tcp_keepalive': True,

                # Timeout settings
                'connect_timeout': 2000, # ms
                'send_timeout': 750 * 1000, # us
                'receive_timeout': 750 * 1000, # us
                '_poll_timeout': 2000, # ms

                # Better failover
                'ketama': True,
                'remove_failed': 1,
                'retry_timeout': 2,
                'dead_timeout': 30,
            }
        }
    }
}
#CACHES = {
#    'default': {
#	'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
#	'LOCATION': [
#	    '127.0.0.1:11211',
#    	]
#    },
#    'redis': {
#	'BACKEND': 'django_redis.cache.RedisCache',
#	'LOCATION': REDIS_CACHE_URL,
#        'OPTIONS': {
#            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
#            'IGNORE_EXCEPTIONS': True,
#        },
#    }
#}

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql',
#        'NAME': 'mydatabase',
#        'USER': 'mydatabaseuser',
#        'PASSWORD': 'mypassword',
#        'HOST': '127.0.0.1',
#        'PORT': '5432',
#    }
#}

#DATABASES['default']['ATOMIC_REQUESTS'] = True  # noqa F405
#DATABASES['default']['CONN_MAX_AGE'] = 60
DATABASES['default'] = dj_database_url.config(conn_max_age=600)
try:
    from .local_settings import *
except ImportError:
    pass

django_heroku.settings(locals())
