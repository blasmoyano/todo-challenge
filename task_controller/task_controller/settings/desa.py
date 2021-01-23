from .settings import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

URL_NAME = 'DESA_control_tareas'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR_SPLIT[0], 'static'),)
STATIC_ROOT = os.path.join(BASE_DIR_SPLIT[0], 'staticfiles')
MEDIA_ROOT = os.path.join(BASE_DIR_SPLIT[0], 'media')
MEDIA_URL = '/'

# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR_SPLIT[0], 'db.sqlite3'),
    }
}

# Login

LOGIN_REDIRECT_URL = "/menu"
LOGOUT_REDIRECT_URL = '/login/'
LOGIN_URL = "/login/"

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',)

# Logging

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': f'{os.path.join(BASE_DIR_SPLIT[0])}/debug.log',
        },
    },
    'root': {
        'handlers': ['file'],
        'level': 'WARNING',
    },
}
