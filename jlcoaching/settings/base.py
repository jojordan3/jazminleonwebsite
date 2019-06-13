"""
Django settings for jlcoaching project.

Generated by 'django-admin startproject' using Django 2.1.8.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

SITE_ID = 1
# Application definition

INSTALLED_APPS = [
    # This project
    'website',
    'blog',
    'contact',
    'documents_gallery',
    'events',
    'gallery',
    'pages',
    'people',
    'products',
    'utils',

    # CodeRed CMS
    'coderedcms',
    'bootstrap4',
    'modelcluster',
    'taggit',
    'wagtailfontawesome',
    'wagtailcache',
    'wagtailimportexport',

    # Wagtail
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.core',
    'wagtail.contrib.settings',
    'wagtail.contrib.modeladmin',
    'wagtail.contrib.table_block',
    'wagtail.admin',

    # Other Wagtail
    'wagtail.contrib.routable_page',
    'wagtail.contrib.sitemaps',
    'wagtail.contrib.search_promotions',
    #'wagtail.contrib.postgres_search',
    'wagtail_feeds',
    'wagtailmarkdown',
    'foundation_formtags',

    # Django
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "django.contrib.sitemaps",
    'django.contrib.sites',

    # Fluent
    #'fluentcms_cookielaw',
    'fluentcms_countdown',
    'fluent_contents',
    'fluent_contents.plugins.code',
    'fluent_contents.plugins.commentsarea',
    #'fluent_contents.plugins.disquswidgets',
    #'fluent_contents.plugins.formdesignerlink',
    'fluent_contents.plugins.gist',
    #'fluent_contents.plugins.googledocsviewer',
    'fluent_contents.plugins.iframe',
    'fluent_contents.plugins.markup',
    'fluent_contents.plugins.rawhtml',
    'fluent_contents.plugins.text',

    'compressor',
    #'whitenoise',
    # Some plugins need extra Django applications
    #'disqus',
    'django_comments',
    'django_wysiwyg',
    #'form_designer',

    #'storages',
    #'django_redis',
    #'anymail',
    'mc_tasklist',
]

MIDDLEWARE = [
    # Save pages to cache. Must be FIRST.
    'wagtailcache.cache.UpdateCacheMiddleware',

    # Common functionality
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.common.CommonMiddleware',

    # Security
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    #'whitenoise.middleware.WhiteNoiseMiddleware',

    # Error reporting. Uncomment this to recieve emails when a 404 is triggered.
    #'django.middleware.common.BrokenLinkEmailsMiddleware',

    # CMS functionality
    'wagtail.core.middleware.SiteMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',

    # Fetch from cache. Must be LAST.
    'wagtailcache.cache.FetchFromCacheMiddleware',
]

ROOT_URLCONF = 'jlcoaching.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'wagtail.contrib.settings.context_processors.settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'jlcoaching.wsgi.application'

use_default_site = True

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',},
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/Los_Angeles'
USE_I18N = False
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
]

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'


# Login
LOGIN_URL = 'wagtailadmin_login'
LOGIN_REDIRECT_URL = 'wagtailadmin_home'

PASSWORD_HASHERS = [
    # https://docs.djangoproject.com/en/dev/topics/auth/passwords/#using-argon2-with-django
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
]

# Wagtail settings
WAGTAIL_SITE_NAME = "Jazmin Leon LLC"
WAGTAIL_ENABLE_UPDATE_CHECK = False

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = 'http://www.jazminleoncoaching.com'


# Bootstrap
BOOTSTRAP4 = {
    # set to blank since coderedcms already loads jquery and bootstrap
    'jquery_url': '',
    'base_url': '',
    # remove green highlight on inputs
    'success_css_class': ''
}


# Tags
TAGGIT_CASE_INSENSITIVE = True
