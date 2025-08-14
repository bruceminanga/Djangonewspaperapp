"""
Base Django settings for the config project.

This file is configured for production readiness. Local development settings
can override these in a 'local.py' file.

For more information on this file, see
https://docs.djangoproject.com/en/stable/topics/settings/
"""

from pathlib import Path
import dj_database_url
from decouple import config

# --------------------------------------------------------------------------
# CORE PATHS & CONFIGURATION
# --------------------------------------------------------------------------

# This points to the project root folder (where manage.py is).
# Path(__file__) -> /.../config/settings/base.py
# .parent -> /.../config/settings/
# .parent -> /.../config/
# .parent -> /.../ (project root)
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Decouple reads secrets from a .env file or environment variables.
# SECRET_KEY *must* be set in your .env file.
SECRET_KEY = config("SECRET_KEY")

# DEBUG defaults to False for security. Set DEBUG=True in your .env for local dev.
DEBUG = config("DEBUG", default=False, cast=bool)

# Define hosts. In .env, this should be a comma-separated string,
# e.g., ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
ALLOWED_HOSTS = config(
    "ALLOWED_HOSTS",
    default="127.0.0.1,localhost",
    cast=lambda v: [s.strip() for s in v.split(",")],
)


# --------------------------------------------------------------------------
# APPLICATION DEFINITION
# --------------------------------------------------------------------------

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # Local Apps
    "pages.apps.PagesConfig",
    "accounts.apps.AccountsConfig",
    "articles.apps.ArticlesConfig",
    # Third-Party Apps
    "crispy_forms",
    "crispy_bootstrap5",
    "django_extensions",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "config.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        # This tells Django to look in a top-level 'templates' folder
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "config.wsgi.application"


# --------------------------------------------------------------------------
# DATABASE
# --------------------------------------------------------------------------
# https://github.com/jazzband/dj-database-url
# Looks for DATABASE_URL in .env. If not found, it uses the default SQLite db.

DATABASES = {
    "default": config(
        "DATABASE_URL",
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        cast=dj_database_url.parse,
    )
}


# --------------------------------------------------------------------------
# PASSWORD VALIDATION
# --------------------------------------------------------------------------
# https://docs.djangoproject.com/en/stable/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"
    },
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]


# --------------------------------------------------------------------------
# INTERNATIONALIZATION & LOCALIZATION
# --------------------------------------------------------------------------
# https://docs.djangoproject.com/en/stable/topics/i18n/

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True  # USE_L10N is deprecated, USE_TZ is the modern standard


# --------------------------------------------------------------------------
# STATIC & MEDIA FILES
# --------------------------------------------------------------------------
# https://docs.djangoproject.com/en/stable/howto/static-files/

STATIC_URL = "/static/"
# Tells Django where to find your static files in development
STATICFILES_DIRS = [BASE_DIR / "static"]
# The single folder where 'collectstatic' will dump all static files for production
STATIC_ROOT = BASE_DIR / "staticfiles"

# For user-uploaded files
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"


# --------------------------------------------------------------------------
# DJANGO PROJECT CONFIGURATION
# --------------------------------------------------------------------------

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
AUTH_USER_MODEL = "accounts.CustomUser"
LOGIN_REDIRECT_URL = "home"
LOGOUT_REDIRECT_URL = "home"

# Crispy Forms
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = "bootstrap5"
