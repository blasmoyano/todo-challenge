from django.conf import settings
from .settings import *
import os

URL_NAME = 'PROD_control_tareas'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = f'{URL_NAME}/static/'
MEDIA_URL = f'{URL_NAME}/media/'

# Login

LOGIN_REDIRECT_URL = "/menu"
LOGOUT_REDIRECT_URL = '/login/'
LOGIN_URL = "/login/"


AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',)
