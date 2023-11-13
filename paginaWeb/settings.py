"""
Django settings for paginaWeb project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

from pathlib import Path
# Variables de entorno
from decouple import config
# Para despliegue
import os
# para despliegue instalar    pip install dj-database-url psycopg2-binary
import dj_database_url

# Para identificar msj de error
from django.contrib.messages import constants as msj_error

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = config("SECRET_KEY")
# Para despliegue
SECRET_KEY = os.environ.get('SECRET_KEY', default='your secret key')
# SECURITY WARNING: don't run with debug turned on in production!
# Se cambia cuando esta en Modo Producción a False
# De string a booleano
#DEBUG = config("DEBUG", cast=bool)
DEBUG = False
# Para despliegue
DEBUG = 'RENDER' not in os.environ

ALLOWED_HOSTS = []

# Para despliegue
RENDER_EXTERNAL_HOSTNAME = os.environ.get('RENDER_EXTERNAL_HOSTNAME')
if RENDER_EXTERNAL_HOSTNAME:    
    ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    # manejo de archivos static
    'whitenoise.runserver_nostatic',
    'django.contrib.staticfiles',
    # aplicaciones del proyecto
    'Apps.pywebApp',
    'Apps.serviciosApp',
    'Apps.blogApp',
    'Apps.contactoApp',
    'Apps.tiendaApp',
    'Apps.carroApp',
    'Apps.autenticaApp',
    'Apps.pedidosApp',
    'Apps.pdfApp',
    # Para manejo Autenticación
    'crispy_forms',
    'crispy_bootstrap5',
    # Django Rest Framework
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',   # Para despliegue
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'paginaWeb.urls'

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
                'django.contrib.messages.context_processors.messages', # para mensajes de error
                'Apps.carroApp.context_processor.importe_carro', # declaración de variable global
            ],
        },
    },
]

WSGI_APPLICATION = 'paginaWeb.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = { # Para despliegue
    'default': dj_database_url.config(        
        # Feel free to alter this value to suit your needs.        
        default='postgresql://postgres:postgres@localhost:5432/mysite', 
            conn_max_age=600)
        #'ENGINE': 'django.db.backends.sqlite3',
        #'NAME': BASE_DIR / 'db.sqlite3',
        #'ENGINE': 'django.db.backends.postgresql_psycopg2',
        #'NAME': config("DB_NAME"),
        #'USER': config("DB_USER"),
        #'PASSWORD': config("DB_PASSWORD"),
        #'HOST': config('ALLOWED_HOSTS', cast=lambda v: [s.strip() for s in v.split(',')]),
        #'HOST': config('ALLOWED_HOSTS'),
        #'DATABASE_PORT': config("DB_DATABASE_PORT", cast=int)
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

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'es-MX'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'

if not DEBUG:
    # Tell Django to copy statics to the `staticfiles` directory
    # in your application directory on Render.
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

    # Turn on WhiteNoise storage backend that takes care of compressing static files
    # and creating unique names for each version so they can safely be cached forever.
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
    
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Para guardar archivos de media en computadora
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# configuración email
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOTS = "smtp.gmail.com"
EMAIL_USE_SSL = config("EMAIL_USE_SSL", cast=bool)
EMAIL_PORT = config('EMAIL_PORT', cast=int)
EMAIL_HOTS_USER = config("EMAIL_HOTS_USER")
EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")

# Para manejo Autenticación
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"

# Para identificar msj de error
MESSAGE_TAGS = {
    msj_error.DEBUG: 'debug',
    msj_error.INFO: 'info',
    msj_error.SUCCESS: 'success',
    msj_error.WARNING: 'warning',
    msj_error.ERROR: 'danger',
}
