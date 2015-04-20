"""
Django settings for echelon project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
from django.conf.global_settings import MIGRATION_MODULES

BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '39*l!u5$be6#f_*nzh@+6(u40ut=#867z@r&m195dcum^_0d^)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admindocs',
    'app',
    'app.subsystem',
    'sslserver',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'echelon.urls'

WSGI_APPLICATION = 'echelon.wsgi.application'

# NOTE:
# To use SSL, uncomment the following lines and run
#  "manage.py runsslserver"
#
# SESSION_COOKIE_SECURE = True
#
# CSRF_COOKIE_SECURE = True
#
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


# Default Login URL
LOGIN_URL='/login_handler/'
# SESSION_EXPIRE_AT_BROWSER_CLOSE=True

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# Note on Databases:
# If you do have a local database, feel free to use it. But for convenience, we will be switching to a centralized one
#        'USER': 'eve',
#         'PASSWORD': 'SOEN341echelon!',
#         'HOST': 'bbbtimmy.noip.me', # OR centcom.noip.me
#         'PORT': '3306',
# Note that the remote DB at centcom.noip.me is 20x slower than having a local DB on your machine

DATABASES = {
    'default': {
        'ENGINE': 'mysql.connector.django',
        'NAME': 'echelon',  # MySQL must contain this DB.
        'USER': 'root',
        'PASSWORD': 'SOEN341echelon!',
        'HOST': 'localhost',
        'PORT': '3306',
        # 'TEST': {
        #     'NAME': 'test_echelon',
        #     'CREATE_DB': 'False',
        #     'CREATE_USER': 'False',
        #     'USER': 'korra',
        #     'PASSWORD': 'SOEN341echelon!',
        #     'TBLSPACE': 'test_echelon',
        #     }
    }
}

# Used for local testing (Put your own user and password
# DATABASES = {
#     'default': {
#         'ENGINE': 'mysql.connector.django',
#         'NAME': 'echelon',  # MySQL must contain this DB.
#         'USER': 'root',
#         'PASSWORD': 'SOEN341echelon!',
#         'HOST': 'localhost',
#         'PORT': '3306',
#         'TEST': {
#             'NAME': 'test_echelon',
#             'CREATE_DB': 'False',
#             'CREATE_USER': 'False',
#             'USER': '????',
#             'PASSWORD': '????',
#         }
#     }
# }

# Logging
#
# The logging system will output a log at various levels ranging from DEBUG to CRITICAL into a file (django-debug.log)
# The default logger that will be used will show a timestamp, the level of the log, and the message attached.
# The possible levels are:
#   - DEBUG: used to follow the actions in debug mode
#   - INFO: used for general system information
#   - WARNING: used to indicate a minor problem
#   - ERROR: used to indicate a a major problem
#   - CRITICAL: used to indicate a critical problem
# To use the logger,
# - import logging into your file
# - make an instance of the logger using:
#       logger = logging.getLogger(__name__)
# - to use the logger:
#       logger.error("This is the message to be transmitted")
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(asctime)s %(levelname)s %(message)s'
        },
    },
    'handlers': {
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': 'django-debug.log',
            'formatter': 'simple',
        },
    },
    'loggers': {
        'app.views': {
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
    },
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'America/Montreal'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'

# email settings:
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'echelonplanner@gmail.com'
EMAIL_HOST_PASSWORD = 'COENmasters'
DEFAULT_FROM_EMAIL = 'echelonplanner@gmail.com'
