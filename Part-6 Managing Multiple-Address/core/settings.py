import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-u++b3(galc2*hl2jom2*l!f=^om@u+#s&+f=pn606*g4e#a5*&"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "store",
    "basket",
    "account",
    "payment",
    "orders",
    "mptt2",
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

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
                "store.context_processors.categories",
                "basket.context_processors.basket",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = "static/"
STATICFILES_DIRS = [BASE_DIR / "static"]


MEDIA_URL = "media/"
MEDIA_ROOT = BASE_DIR / "media"

# Basket session ID
BASKET_SESSION_ID = "basket"

# Custom user model
AUTH_USER_MODEL = "account.Customer"
LOGIN_REDIRECT_URL = "/account/dashboard"
LOGIN_URL = "/account/login/"

# Stripe Payment
os.environ.setdefault(
    "STRIPE_PUBLISHABLE_KEY",
    "pk_test_51NXOYVD4BhLDGloIZC8jIYkNLBBaI3Pm3IHc1jZ1j3hpVL4dA8k0fmhddAewyVZ00qhsCkTM84HeYNUo1roI5zZp00514GJx8c",
)
# PUBLISHABLE_KEY = 'pk_test_51NXOYVD4BhLDGloIZC8jIYkNLBBaI3Pm3IHc1jZ1j3hpVL4dA8k0fmhddAewyVZ00qhsCkTM84HeYNUo1roI5zZp00514GJx8c'
STRIPE_SECRET_KEY = "sk_test_51NXOYVD4BhLDGloILB9pzzji8QcYttcHvtzc3dhQ34lmtVMglLA2KydiJaGI0e0JL9MTJplFEOd1qZZtf7O5ELFh00uMmwNxNa"
STRIPE_ENDPOINT_SECRET = (
    "whsec_811486aec38b39c30dbeac5d9ef9dbb41be7933e35bdd81030340e91f720a6bc"
)
# stripe listen --forward-to localhost:8000/payment/webhook/

# Email setting
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
