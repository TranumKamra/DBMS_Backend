"""
Django settings for osapi project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-qm#_rn@(8pwxal#0e=2+^1(-6vri_^jx*k)!)#dy0!orl_qia*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

CORS_ALLOW_ALL_ORIGINS = False
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",  # Add the origin you want to allow
]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'apis',
    'corsheaders',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'osapi.urls'

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

WSGI_APPLICATION = 'osapi.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'quiz2',
        'USER': 'root',
        'PASSWORD': '30112002',
        'HOST': 'localhost',  # Set to the address of your MySQL server
        'PORT': '3306',      # Set to the port your MySQL server is running on
        'POOL': {
            'max_overflow': 10,
            'overflow_timeout': 60,
        },
    },
    'main': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'INVENTORY',
        'USER': 'root',
        'PASSWORD': '30112002',
        'HOST': 'localhost',   
        'PORT': '3306',
        'POOL': {
            'max_overflow': 10,
            'overflow_timeout': 60,
        },
    },
    'read1': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'INVENTORY_READ1',
        'USER': 'root',
        'PASSWORD': '30112002',
        'HOST': 'localhost',  
        'PORT': '3306',
        'POOL': {
            'max_overflow': 10,
            'overflow_timeout': 60,
        },
    },
    'read2': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'INVENTORY_READ2',
        'USER': 'root',
        'PASSWORD': '30112002',
        'HOST': 'localhost',  
        'PORT': '3306',
        'POOL': {
            'max_overflow': 10,
            'overflow_timeout': 60,
        },
    },
    'read3': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'INVENTORY_READ3',
        'USER': 'root',
        'PASSWORD': '30112002',
        'HOST': 'localhost',  # Set to the address of your MySQL server
        'PORT': '3306',
        'POOL': {
            'max_overflow': 10,
            'overflow_timeout': 60,
        },
    },
    'write': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'INVENTORY',
        'USER': 'root',
        'PASSWORD': '30112002',
        'HOST': 'localhost',  # Set to the address of your MySQL server
        'PORT': '3306',
        'POOL': {
            'max_overflow': 10,
            'overflow_timeout': 60,
        },
    },
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
