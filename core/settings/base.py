"""
Django settings for wf_website project.

Generated by 'django-admin startproject' using Django 2.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys
from decouple import config



from django.core.management.utils import get_random_secret_key

from braintree import Configuration as BraintreeConfiguration
from braintree import Environment as BraintreeEnvironment

import dj_database_url

from dotenv import load_dotenv

load_dotenv()

#default_allowed_hosts = "127.0.0.1 ,localhost"

#ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", default_allowed_hosts).split(",")
# ALLOWED_HOSTS =['*']

ALLOWED_HOSTS = ['coral-app-22swg.ondigitalocean.app','127.0.0.1', 'localhost', 'www.spotlightkenya.club', 'spotlightkenya.club']
#default_csrf_trusted_origins = "http://127.0.0.1,https://127.0.0.1,http://localhost,https://localhost,https://SpotlightKenya.ngrok.io"
CSRF_TRUSTED_ORIGINS=['https://coral-app-22swg.ondigitalocean.app/','http://127.0.0.1','https://www.spotlightkenya.club/','https://spotlightkenya.club/']
#CSRF_TRUSTED_ORIGINS = os.getenv(
#    "CSRF_TRUSTED_ORIGINS", default_csrf_trusted_origins
#).split(",")

PROJECT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE_DIR = os.path.dirname(PROJECT_DIR)

#SECURE_REFERRER_POLICY = "strict-origin"
# DATABASES['default'] = dj_database_url.config(conn_max_age=600, ssl_require=True)

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", get_random_secret_key())

DEBUG = os.getenv("DEBUG", "False")

# Settings related to DigitalOcean Spaces

#STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')

AUTH_USER_MODEL = "accounts.User"

CART_SESSION_ID = "cart"
LOGIN_URL = "/login/"
# Braintree settings
# BRAINTREE_MERCHANT_ID = os.getenv("BRAINTREE_MERCHANT_ID")
# BRAINTREE_PUBLIC_KEY = os.getenv("BRAINTREE_PUBLIC_KEY")
# BRAINTREE_PRIVATE_KEY = os.getenv("BRAINTREE_PRIVATE_KEY")
#
# BraintreeConfiguration.configure(
#     BraintreeEnvironment.Sandbox,
#     BRAINTREE_MERCHANT_ID,
#     BRAINTREE_PUBLIC_KEY,
#     BRAINTREE_PRIVATE_KEY,
# )
# SESSION_COOKIE_AGE = 60 * 60 * 24 * 7  # 1 week in seconds

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/


# Application definition

INSTALLED_APPS = [
    'wagtail',


    "accounts",
    "addresses",

    "cart",
    "community",
    "contact",
    "content_migration",


    "documents",
    "donations",
    "blogs",
    
    "facets",
    "forms",
    "home",
    "library",
    "memorials",
    "navigation",

    "orders",
    "payment.apps.PaymentConfig",
    "search",
    "store",
    "subscription",
    "magazine",
    "streams",
    'django_comments',
    "wagtailpod",
    "hitcount",


    #'core.blog',
    #'custom_comments',


    "wf_pages",
    "wagtail.contrib.forms",
    "wagtail.contrib.modeladmin",
    "wagtail.contrib.redirects",
    "wagtail.contrib.routable_page",
    "wagtail.contrib.settings",
    "wagtail.contrib.styleguide",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",

    "modelcluster",
    "taggit",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.sitemaps",
    'django.contrib.sites',

    "crispy_forms",
    "django_flatpickr",
    "storages",
    "wagtail_color_panel",
    "wagtailfontawesome",
    "wagtailmedia",
]


CRISPY_TEMPLATE_PACK = "bootstrap4"

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]
# class DisableMIMETypesMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response
#
#     def __call__(self, request):
#         response = self.get_response(request)
#         response['X-Content-Type-Options'] = 'nosniff'
#         return response
#
# MIDDLEWARE.insert(1, 'DisableMIMETypesMiddleware')

X_FRAME_OPTIONS = "SAMEORIGIN"

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(PROJECT_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "wagtail.contrib.settings.context_processors.settings",
            ]
        },
    }
]

WSGI_APPLICATION = "core.wsgi.application"


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases


from .cdn.conf import *  #noqa

NOT_COLLECTING_STATICFILES = len(sys.argv) > 0 and sys.argv[1] != "collectstatic"

#
# DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql_psycopg2',
#             'NAME': os.getenv('DB_NAME'),
#             'HOST': 'localhost',
#             'USER': os.getenv('DB_USER'),
#             'PASSWORD': os.getenv('DB_PASSWORD'),
#             'PORT': '',
#         }
#     }


DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

WAGTAILSEARCH_BACKENDS = {
    "default": {
        "BACKEND": "wagtail.search.backends.database",
    }
}
STATIC_URL = '/static/'

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

LOGIN_REDIRECT_URL = "/"
LOGIN_URL = '/login/'
# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

STATICFILES_DIRS = [os.path.join(PROJECT_DIR, "static")]

# if USE_SPACES:
#     STATIC_URL = f"{AWS_S3_ENDPOINT_URL}/{ AWS_STORAGE_BUCKET_NAME }/{AWS_LOCATION}/"
#     STATICFILES_STORAGE = "core.storage_backends.StaticStorage"
#
#     MEDIA_URL = (
#         f"{AWS_S3_ENDPOINT_URL}/{ AWS_STORAGE_BUCKET_NAME }/{PUBLIC_MEDIA_LOCATION}/"
#     )
#     DEFAULT_FILE_STORAGE = "core.storage_backends.MediaStorage"
#
#     # Prevent setting URL querystring parameters
#     # which are causing 403 errors on DigitalOcean Spaces
#     AWS_QUERYSTRING_AUTH = False
# else:
#     STATIC_URL = "/static/"
#     MEDIA_ROOT = os.path.join(BASE_DIR, "media")
#     MEDIA_URL = "/media/"


# Wagtail settings

WAGTAIL_SITE_NAME = "Spotlight Kenya"

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = "http://spotlightkenya.club"

#EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
#CRISPY_ALLOWED_TEMPLATE_PACKS = "tailwind"
#CRISPY_TEMPLATE_PACK = "tailwind"

# DO NOT use on production, test key is available in the URL below
# https://developers.google.com/recaptcha/docs/faq
# RECAPTCHA_PUBLIC_KEY = "6LeIxAcTAAAAAJcZVRqyHh71UMIEGNQ_MXjiZKhI"
# RECAPTCHA_PRIVATE_KEY = "6LeIxAcTAAAAAGG-vFI1TnRWxMZNFuojJ4WifJWe"
# NOCAPTCHA = True
# SILENCED_SYSTEM_CHECKS = ["captcha.recaptcha_test_key_error"]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

SITE_ID = 1

#COMMENTS_APP = 'custom_comments'
# WAGTAILADMIN_BASE_URL = '/admin/'
# APPEND_SLASH = False

WAGTAILADMIN_BASE_URL = '/staffarea'
# WAGTAIL_FRONTEND_LOGIN_URL = '/accounts/login/'
WAGTAIL_FRONTEND_LOGIN_URL = '/staffarea/login/'

# COLLECTFAST_STRATEGY = "collectfast.strategies.filesystem.FileSystemStrategy"
# COLLECTFAST_ENABLED = False
SECURE_CONTENT_TYPE_NOSNIFF = True



EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'spotlightkenya7@gmail.com'
EMAIL_HOST_PASSWORD = 'aryb pjzq mchf rnpl'
EMAIL_PORT = '587'
EMAIL_USER_TLS = True
EMAIL_USER_SSL = True
DEFAULT_FROM_EMAIL = 'www@spotlightkenya.club'
DEFAULT_TO_EMAIL = 'spotlightkenya7@gmail.com'
EMAIL_TO = 'spotlightkenya7@gmail.com'
