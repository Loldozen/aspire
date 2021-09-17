from aspire.settings.base import *
import os


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'HOST': 'localhost',
        'USER': 'aspire_dev',
        'NAME': 'aspire',
        'PASSWORD': 'password',
        'PORT': 5432,
    },
}

"""DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}"""


ALLOWED_HOSTS=['*']

DEBUG = bool(int(os.environ.get('DEBUG', 0)))

BACKEND_URL = 'http://localhost:8000'

AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')

# #############  JWT #########################################
JWT_SECRET_KEY = 'n]>>JF6PrP@PbyZ%$Q@B'
JWT_ALGO = 'HS256'