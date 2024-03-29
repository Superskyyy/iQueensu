"""
Django settings for iQueensu project.

Generated by 'django-admin startproject' using Django 2.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os
import platform

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# sys.path.insert(0, os.path.join(BASE_DIR, 'apps\\test_apps'))
# print(sys.path)


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "l=zqe8o+tt8v6fyd*q-0+1_+_1440a$vmi--5vomh*j1jy4p8w"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Turn LOCAL_DEBUG on if you want to debug frontend using npm start

my_os = platform.system()
LOCAL_DEBUG = True
if my_os != "Linux":
    LOCAL_DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    "QAPI.apps.QapiConfig",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.postgres",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "django_filters",
    "corsheaders",
]

INSTALLED_APPS += [
    'djoser'
]

# # apps for auth purposes
# INSTALLED_APPS += [
#     'rest_framework.authtoken',
#     'rest_auth',
#     'django.contrib.sites',
#     'allauth',
#     'allauth.account',
#     'rest_auth.registration',
#     'QUser',
# ]

# app for Qcumber
INSTALLED_APPS += ["QCumber"]

# for all-auth usage:
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
SITE_ID = 1
# AUTH_USER_MODEL = 'QUser.CustomUser'

# register our apps here ^^

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

"""
if LOCAL_DEBUG:
    MIDDLEWARE = [
        "corsheaders.middleware.CorsMiddleware",
        "django.middleware.common.CommonMiddleware",
    ]


# 730cc199a04d792a9f77046c59edf6a73a30a135

"""

ROOT_URLCONF = "iQueensu.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": ["templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ]
        },
    }
]

WSGI_APPLICATION = "iQueensu.wsgi.application"

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

# This can be used to toggle between your local testing db (db.sqlite3) and the PostgreSQL backend:
DOCKER = True

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases
if DOCKER:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql",
            "NAME": "postgres",
            "USER": "postgres",
            "PASSWORD": "iqueensu",
            "HOST": "db",
            "PORT": 5432,
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": os.path.join(BASE_DIR, "db.sqlite3"),
        }
    }

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

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "EST"

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(BASE_DIR, "static")
# STATIC_ROOT = "/root/iQueensu/static"
# STATICFILES_DIRS = [
#           os.path.join(BASE_DIR, "static"),
#          ]
"""
# RestAPI configurations
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend'),
    'PAGE_SIZE': 10
}
"""

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}

SIMPLE_JWT = {
   'AUTH_HEADER_TYPES': ('JWT',),
}

REST_API_ADDRESS = "qapi_v0"

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
