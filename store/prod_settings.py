import os
import dj_database_url

from .settings import *

SECRET_KEY = os.environ.get('SECRET_KEY')

DEBUG = True

ALLOWED_HOSTS = ['.herokuapp.com', ]


DATABASES = {
    'default': dj_database_url.config(default=os.environ.get('DATABASE_URL'))
}
