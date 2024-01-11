import os
from pathlib import Path
from dotenv import load_dotenv



load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')

NAME = os.getenv('NAME')
USER = os.getenv('USER')
PASSWORD = os.getenv('PASSWORD')
HOST = os.getenv('HOST')
PORT = os.getenv('PORT')

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = SECRET_KEY
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1']


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': NAME,
        'USER': USER,
        'PASSWORD': PASSWORD,
        'HOST': HOST,
        'PORT': PORT,
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, 'static')