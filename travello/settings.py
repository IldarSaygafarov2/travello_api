import datetime
import os

from pathlib import Path

from dotenv import load_dotenv

load_dotenv()

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-za7%24*32r%#r$!^25znrlooo5=5sz=dh(owsph%7f!g^z9&b$'

DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    '176.96.243.220',
    'travella-admin.uz',
    'travellatestapi.pythonanywhere.com'
]

INSTALLED_APPS = [
    'jazzmin',
    'modeltranslation',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    # 'rest_framework.authtoken',
    'rest_framework_simplejwt',
    'drf_spectacular',
    'ckeditor',
    'nested_inline',
    'django_filters',
    'corsheaders',
    'constance',

    'apps.users_auth.apps.UsersAuthConfig',
    'apps.users.apps.UsersConfig',
    'apps.user_route.apps.UserRouteConfig',
    'apps.articles.apps.ArticlesConfig',
    'apps.reviews.apps.ReviewsConfig',
    'apps.events.apps.EventsConfig',
    'apps.main.apps.MainConfig',
    'apps.hotels.apps.HotelsConfig',
    'apps.corporate_clients.apps.CorporateClientsConfig',
    'apps.tours_favorites.apps.ToursFavoritesConfig',
    'apps.tours_booked.apps.ToursBookedConfig',
    'apps.roles.apps.RolesConfig',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'travello.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates'
        ],
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

WSGI_APPLICATION = 'travello.wsgi.application'

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

LANGUAGE_CODE = 'ru'
gettext = lambda s: s
LANGUAGES = (
    ('ru', gettext('Russian')),
    ('uz', gettext('Uzbek')),
    ('en', gettext('English')),

)
MODELTRANSLATION_TRANSLATION_FILES = (
    'apps.articles.translation',
    'apps.corporate_clients.translation',
    'apps.events.translation',
    'apps.hotels.translation',
    'apps.main.translation',
    'apps.reviews.translation',
)
# MODELTRANSLATION_DEFAULT_LANGUAGE = 'ru'

LOCALE_PATHS = [BASE_DIR / 'locale']

TIME_ZONE = 'Asia/Tashkent'

USE_I18N = True

USE_TZ = True

STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# custom settings

AUTH_USER_MODEL = 'users.User'
REST_FRAMEWORK = {
    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
    ),
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = False
EMAIL_PORT = 465
EMAIL_USE_SSL = True
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD')

SMS_API_EMAIL = os.getenv('SMS_API_EMAIL')
SMS_API_KEY = os.getenv('SMS_API_KEY')
SMS_API_URL = os.getenv('SMS_API_URL')

API_URL = os.getenv('API_URL')

INSTAGRAM_APP_ID = os.getenv('INSTAGRAM_APP_ID')
INSTAGRAM_APP_CLIENT_ID = os.getenv('INSTAGRAM_APP_CLIENT_ID')


CORS_ALLOW_ALL_ORIGINS = True
CSRF_TRUSTED_ORIGINS = [
    'https://travella-admin.uz'
]

CURRENCY_API_KEY = os.getenv('CURRENCY_API_KEY')
BOT_TOKEN = os.getenv('BOT_TOKEN')
SECOND_BOT_TOKEN = os.getenv('SECOND_BOT_TOKEN')
CHANNEL_CHAT_ID = os.getenv('CHANNEL_CHAT_ID')
SECOND_CHANNEL_CHAT_ID = os.getenv('SECOND_CHANNEL_CHAT_ID')
TG_API_URL = 'https://api.telegram.org/bot{token}/sendMessage?chat_id={channel_id}&text={text}'


JAZZMIN_SETTINGS = {
    'language_chooser': True
}


# Constance django
CONSTANCE_CONFIG = {
    'MAP_CODE': ('Office map', ''),
}
CONSTANCE_BACKEND = 'constance.backends.database.DatabaseBackend'

SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': datetime.timedelta(minutes=60),
    'REFRESH_TOKEN_LIFETIME': datetime.timedelta(days=1),
}