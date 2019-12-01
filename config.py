import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DEBUG = os.environ.get('DEBUG')
    HOST = os.environ.get('HOST')
    DATABASE_URL = os.environ.get('DATABASE_URL') or 'postgres://oholkjlekcyeki:5ce0c19497d9f781f6c1d1a172444d1e861fed1a8f5a7bc7aea2b00cfd5548cc@ec2-174-129-214-193.compute-1.amazonaws.com:5432/derf5i0bvu168'