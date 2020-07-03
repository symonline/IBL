import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

class Config(object):
    
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DEBUG = os.environ.get('DEBUG')
    HOST = os.environ.get('HOST')
    DATABASE_URL = os.environ.get('DATABASE_URL') or 'postgres://aeolghqbxijwhs:3276aad73bb4ba5e8e4a8a3a4e40dc79ed7d93d85a7cd4c5e70742e3bac5ed86@ec2-46-51-190-87.eu-west-1.compute.amazonaws.com:5432/d7d90ifqq940ed'