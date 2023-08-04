
from datetime import timedelta
from pathlib import Path
import os

from dotenv import load_dotenv
load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = []

BASE_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MY_APPS = [
    'apps.portafolio',
    'apps.tasks',
    'apps.posts',
]

THIRDS_APPS = [
    'rest_framework',
    'rest_framework_simplejwt',
    'rest_framework_simplejwt.token_blacklist',
    'drf_yasg',
]

INSTALLED_APPS = BASE_APPS + MY_APPS + THIRDS_APPS


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',

    'corsheaders.middleware.CorsMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



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
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'dist/static')
]

MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')


# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

SWAGGER_SETTINGS = {
    'DOC_EXPANSION': 'none',
}


AUTH_USER_MODEL = 'portafolio.User'


CORS_ALLOWED_ORIGINS = [
    'http://localhost:5173',
]

CORS_ALLOW_CREDENTIALS = True


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
  }

SIMPLE_JWT = {
      'ACCESS_TOKEN_LIFETIME': timedelta(hours=5),
      'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
      'ROTATE_REFRESH_TOKENS': True,
      'BLACKLIST_AFTER_ROTATION': True,

      'ALGORITHM': 'HS256',
      'VERIFYING_KEY': SECRET_KEY,
      'AUDIENCE': None,
      'ISSUER': None,
      'JWT_URL': None,
      'LEEWAY': 0,

      'AUTH_HEADER_TYPES': ('Bearer',),
      'AUTH_HEADER_NAME': 'HTTP_AUTHORIZATION',
      'USER_ID_FIELD': 'id',
      'USER_ID_CLAIM': 'user_id',

      'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
      'TOKEN_TYPE_CLAIM': 'token_type',
      'TOKEN_USER_CLAIM': 'rest_framework_simplejwt.models.TokenUser',

      'JTI_CLAIM': 'jti',
  }

