import os


DEBUG = True

SERVER_NAME = 'localhost:8000'
SECRET_KEY = os.environ['SECRET_KEY']

db_uri = 'postgresql://{0}:{1}@postgres:5432/{2}'.format(os.environ['POSTGRES_USER'],
                                                         os.environ['POSTGRES_PASSWORD'],
                                                         os.environ['POSTGRES_DB'])

SQLALCHEMY_DATABASE_URI = db_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False

SEED_USER_EMAIL = 'dev@local.host'
SEED_USER_USERNAME = 'dev'
SEED_USER_PASSWORD = os.environ['SEED_USER_PASSWORD']