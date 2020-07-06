import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DEBUG = os.environ.get('DEBUG')
    HOST = os.environ.get('HOST')
    DATABASE_URL = os.environ.get('DATABASE_URL_LOC') or os.environ.get('HEROKU_POSTGRESQL_ORANGE_URL') 