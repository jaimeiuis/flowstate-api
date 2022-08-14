import os
from dotenv import load_dotenv


load_dotenv()


DEBUG = True

SERVER_NAME = 'localhost:8000'
SECRET_KEY = os.getenv('SECRET_KEY')

db_uri = 'postgresql://{0}:{1}@postgres:5432/{2}'.format(os.getenv('POSTGRES_USER'),
                                                         os.getenv('POSTGRES_PASSWORD'),
                                                         os.getenv('POSTGRES_DB'))

SQLALCHEMY_DATABASE_URI = db_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False

SEED_USER_EMAIL = 'dev@local.host'
SEED_USER_USERNAME = 'dev'
SEED_USER_PASSWORD = os.getenv('SEED_USER_PASSWORD')