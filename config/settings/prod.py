import os
from .base import *
import pprint
pprint.pprint(dir())

# static files
INSTALLED_APPS += [    
    "whitenoise.runserver_nostatic",   
]

MIDDLEWARE += [
    #'allauth.account.middleware.AccountMiddleware',
]


STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {  
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",  # new
    },
}


DEBUG = True

ADMINS = [
    ('Bruce Minanga', 'bruceminanga@gmail.com'),
]

ALLOWED_HOSTS = ['newspaperapp.nurseprofessors.com']

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
  'default': {
      'ENGINE': 'django.db.backends.postgresql_psycopg2',
      'NAME': os.getenv('DB_NAME'),
      'USER': os.getenv('DB_USER'),
      'PASSWORD': os.getenv('DB_PASSWORD'),
      'HOST': '127.0.0.1',
      'PORT': '5432',
  }
}