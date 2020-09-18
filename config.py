import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DEBUG = False
    HOST = os.environ.get('HOST')
    SQLALCHEMY_DATABASE_URI = os.environ.get('HEROKU_POSTGRESQL_ORANGE_URL')  # or os.environ.get('HEROKU_POSTGRESQL_ORANGE_URL') 
    SQLALCHEMY_TRACK_MODIFICATIONS = False
