import os
from pathlib import Path

# NOTICE!
# See root `/src/docker-compose.yml` for service settings!
# All stuff should be grabben from there!

# Paths.
APPEND_SLASH = True
PREPEND_WWW = False

# Email.
DEFAULT_FROM_EMAIL = os.environ.get("MAIL_FROM")
# Host.
EMAIL_HOST = os.environ.get("MAIL_HOST")
EMAIL_HOST_USER = os.environ.get("MAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("MAIL_HOST_PASSWORD")
# Auth backend.
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"


# Development.
SECRET_KEY = os.environ.get("SECRET_KEY")
DEBUG = os.environ.get("DEBUG", "true")
DEBUG = (DEBUG == "1" or DEBUG == "true")
ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "*").split() or "*"
FRONTEND_DOMAIN = os.environ.get("FRONTEND_DOMAIN") or "http://localhost:3000"

# Auth service logic.
AUTH_SERVICE_VK_CLIENT_ID = os.environ.get("VK_CLIENT_ID")
AUTH_SERVICE_VK_CLIENT_SECRET = os.environ.get("VK_CLIENT_SECRET")
AUTH_SERVICE_VK_SCHEME = os.environ.get("VK_HTTP_SCHEME")

# Database.
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_NAME'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('POSTGRES_HOST'),
    },
}

# Other.
USE_X_FORWARDED_HOST = True
WSGI_APPLICATION = 'notes_web.wsgi.application'

# Django.
AUTH_USER_MODEL = 'auth_api.User'
INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',

    'rest_framework',
    'rest_framework.authtoken',

    'auth_api.apps.AuthApiConfig',
    'notes_api.apps.NotesApiConfig',
]
MIDDLEWARE = [
    'cors_middleware.core.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}

# Files.
ROOT_URLCONF = 'notes_web.urls'
BASE_DIR = Path(__file__).resolve().parent.parent
STATIC_URL = 'static/'
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

# Language.
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_TZ = True
