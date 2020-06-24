from dotenv import load_dotenv
load_dotenv()

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


PASSWORD = os.getenv("DB_PASSWORD")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'djangoblog',
        'USER': 'postgres',
        'PASSWORD': PASSWORD,
        'HOST': 'localhost',
        'PORT': '5432'
    }
}

DEBUG = True