import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DEBUG = os.environ.get('DEBUG')
    HOST = os.environ.get('HOST')
    DATABASE_URL = os.environ.get('DATABASE_URL') or 'postgres://uc4v16g50tov06:p370bbdeae5f5eb7ff404e011d9496b165eec5e5dd32baf764e990c7b908168e0@ec2-54-164-183-51.compute-1.amazonaws.com:5432/db4lfpbrveq0mq'