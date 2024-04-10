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

ALLOWED_HOSTS = ['nurseprofessors.com', 'www.nurseprofessors.com']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# DATABASES = {
#   'default': {
#       'ENGINE': 'django.db.backends.postgresql',
#       'NAME': os.environ.get('POSTGRES_DB'),
#       'USER': os.environ.get('POSTGRES_USER'),
#       'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
#       'HOST': 'db',
#       'PORT': 5432,
#   }
# }