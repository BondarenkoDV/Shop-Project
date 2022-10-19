import os.path
from pathlib import Path

CART_SESSION_ID = 'cart'
FAVOURITE_SESSION_ID = 'favourite'

BASE_DIR = Path(__file__).resolve().parent.parent

# Stripe Secret Keys

STRIPE_PUBLIC_KEY = 'pk_test_51LhYgWJFj22Bqy6ctwQXJUrFpLVdiQJr8d6BpJoYwDo8HUUPpZ8ZPY8SCWEj6bZ0Qaz2kBQBEuPAxqvnbQFCTUcn00BQDjGxVE'
STRIPE_SECRET_KEY = 'sk_test_51LhYgWJFj22Bqy6cRB283BctANe3eVer6ovD25feU6EvusQwRlcRiDvI4DI8MLW3QFzRv2NF6Feu05cJ1sW9FMw000yrsKYHYP'

# Django Secret Key

SECRET_KEY = 'django-insecure-f@hdcudbj)ift*+w1!*p6+^hsd-@1u!c(wmw+#fj!_tg_u&4@v'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = ''  # Введите хоста почты
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True
EMAIL_PORT = 465
EMAIL_HOST_USER = ''  # Введите почту с которой будет идти рассылка
EMAIL_HOST_PASSWORD = ''  # Введите пароль к этой почте
SERVER_EMAIL = EMAIL_HOST_USER
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'cart.apps.CartConfig',
    'payments.apps.PaymentsConfig',
    'favourites.apps.FavouritesConfig',
    'ShopApp.apps.ShopappConfig',
    'feedback.apps.FeedbackConfig',
    'account.apps.AccountConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'ShopSite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'cart.context_processors.cart',
            ],
        },
    },
]

WSGI_APPLICATION = 'ShopSite.wsgi.application'

'''
PostgreSQL
Заполните следующие поля
Name: Название базы данных
User: Пользователя
Password: Пароль
Host: Сервер
Port: Порт
'''
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
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

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATICFILES_DIRS = []

MEDIA_ROOT = os.path.join(BASE_DIR, ' media')
MEDIA_URL = '/media/'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
