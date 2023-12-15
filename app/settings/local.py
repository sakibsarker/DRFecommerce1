
from .base import *
from dotenv import load_dotenv
import os
load_dotenv()

DATABASES = {
    'default': {
        'ENGINE':'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}