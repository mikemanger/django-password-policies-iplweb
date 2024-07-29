import os

DEBUG = False

LANGUAGES = (("en", "English"),)

LANGUAGE_CODE = "en"

USE_TZ = False
# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

SECRET_KEY = "fake-key"

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.messages",
    "password_policies",
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
        "TEST_NAME": ":memory:",
        "USER": "",
        "PASSWORD": "",
        "PORT": "",
    },
}

ROOT_URLCONF = "password_policies.tests.urls"

SITE_ID = 1

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(os.path.dirname(__file__), "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.i18n",
                "django.contrib.messages.context_processors.messages",
                "password_policies.context_processors.password_status",
            ],
        },
    },
]

MIDDLEWARE = (
    "django.middleware.common.CommonMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "password_policies.middleware.PasswordChangeMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
)

SESSION_SERIALIZER = "django.contrib.sessions.serializers.JSONSerializer"


MEDIA_URL = "/media/somewhere/"

DEFAULT_AUTO_FIELD = "django.db.models.AutoField"
