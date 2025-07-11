"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 5.1.6.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.getenv('SECRET_KEY','asdfasdfasdf')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
     'rest_framework',
     'app',
]
# Allow secure cookies
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Allow frontend domain to access backend cookies
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOWED_ORIGINS = [
    "https://brototype.localhost.com",  # Change this to match your frontend
]

# If using CORS_ALLOW_ALL_ORIGINS (not recommended)
CORS_ALLOW_ALL_ORIGINS = False

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'app.middlewares.TenantMiddleware'
]

import re

# ✅ Allow localhost and any subdomain like agency.localhost:3000
CORS_ALLOWED_ORIGIN_REGEXES = [
    r"^https?://localhost(:\d+)?$",  # Match HTTP & HTTPS localhost
    r"^https?://([a-zA-Z0-9-]+)\.frontend\.localhost(:\d+)?$",  # Subdomains under frontend.localhost
    r"^https?://([a-zA-Z0-9-]+)\.localhost(:\d+)?$",  # Any subdomain under localhost
]

# ✅ Include all subdomains in CSRF_TRUSTED_ORIGINS
CSRF_TRUSTED_ORIGINS = [
    "http://localhost:3000",
    "https://localhost:3000",
    "http://brototype.localhost:3000",
    "https://brototype.localhost:3000",
    "http://frontend.localhost:3000",
    "https://frontend.localhost:3000",
]

# ✅ Allow important headers
CORS_ALLOW_HEADERS = [
    "content-type",
    "authorization",
    "x-csrftoken",
    "x-requested-with",
    "accept",
    "accept-encoding",
    "origin",
]

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "https://localhost:3000",
    "http://brototype.localhost:3000",
    "https://brototype.localhost:3000",
]


# ✅ Allow credentials (for authentication)
CORS_ALLOW_CREDENTIALS = True


ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'
# AUTH_USER_MODEL = 'app.User'

AUTH_USER_MODEL = "app.User"

# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '{asctime} - {levelname} - {module} - {message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} - {message}',
            'style': '{',
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'filename': 'django.log',  # Log file
            'formatter': 'verbose',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file', 'console'],
            'level': 'INFO',
            'propagate': True,
        },
        'custom_logger': {  
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': False,
        },
    },
}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'user_service',
        'USER': os.getenv('DB_NAME' , 'rootuser'),
        'PASSWORD': os.getenv('DB_PASSWORD' , 'rootpassword'),
        'HOST': os.getenv('DB_HOST','roothost'),  
        'PORT': '5432',
    }
}
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'app.authenticate.CustomJwtAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.UserRateThrottle',
        'rest_framework.throttling.AnonRateThrottle',
    ],
    'DEFAULT_THROTTLE_RATES': {
        'user': '20/min',
        'anon': '10/min',
    }
}

# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
