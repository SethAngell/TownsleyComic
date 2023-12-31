import os

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY", "a-super-insecure-key-for-dev-work")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(int(os.environ.get("DJANGO_DEBUG", 1)))

ALLOWED_HOSTS = os.environ.get("ALLOWED_HOSTS", "*").split(" ")


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # 1st Party Apps
    "accounts",
    "content",
    "comic",
    "config",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "config.middleware.SemanticVersionProvider.SemanticVersionProvider",
    "config.middleware.FeatureFlagProvider.FeatureFlagProvider",
]

ROOT_URLCONF = "townsley.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = "townsley.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": "data/townsley.db",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

# ==================================
# = = = User Accounts Settings = = =
AUTH_USER_MODEL = "accounts.CustomUser"

# =======================================
# = = = Static and Media Management = = =
if bool(int(os.environ.get("USE_S3", 0))):
    AWS_ACCESS_KEY_ID = os.environ.get("S3_KEY")
    AWS_SECRET_ACCESS_KEY = os.environ.get("S3_SECRET_KEY")
    AWS_STORAGE_BUCKET_NAME = "townsley"
    AWS_S3_ENDPOINT_URL = (
        "https://f35295ca4b5593f15d54cf0ca7041025.r2.cloudflarestorage.com/"
    )
    AWS_S3_CUSTOM_DOMAIN = "townsley.cdn.thegoodinternet.org"
    AWS_DEFAULT_ACL = "public-read"
    AWS_S3_SIGNATURE_VERSION = "s3v4"

    # Static Config
    STATIC_LOCATION = "static"
    STATICFILES_STORAGE = "townsley.storage_backends.StaticStorage"
    STATIC_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}{STATIC_LOCATION}/"

    # Media Config
    PUBLIC_MEDIA_LOCATION = "media"
    MEDIA_URL = f"https://{AWS_S3_CUSTOM_DOMAIN}{PUBLIC_MEDIA_LOCATION}/"
    DEFAULT_FILE_STORAGE = "townsley.storage_backends.PublicMediaStorage"

    # Remove query string from the url
    AWS_QUERYSTRING_AUTH = False

else:
    STATIC_URL = "static/"
    STATIC_ROOT = os.path.join("static")
    MEDIA_URL = "media/"
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")

STATICFILES_DIRS = [BASE_DIR / "project_static", f"{BASE_DIR}/comic"]

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

INTERNAL_IPS = ("127.0.0.1", "172.20.0.1", "172.21.0.3")

# ===============================
# = = = Deployment Settings = = =
if DEBUG is False:
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_HSTS_SECONDS = 36000
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_SSL_REDIRECT = True
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    X_FRAME_OPTIONS = "DENY"
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "handlers": {
            "console": {"class": "logging.StreamHandler"},
            "file": {
                "level": "DEBUG",
                "class": "logging.FileHandler",
                "filename": "debug.log",
            },
        },
        "loggers": {
            "django": {
                "handlers": ["file", "console"],
                "level": "DEBUG",
                "propagate": True,
            },
        },
    }
