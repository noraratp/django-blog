from .base import *

import os

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('POSTGRES_DATABASE','postgres'),
        'USER': os.environ.get('POSTGRES_USER','postgres'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD','password'),
        'HOST': os.environ.get('POSTGRES_HOST','db'),
        'PORT': os.environ.get('POSTGRES_PORT','5432'),
    }
}
