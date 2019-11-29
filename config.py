import os

class Config(object):
    
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DEBUG = os.environ.get('DEBUG')
    HOST = os.environ.get('HOST')
    
    '''
     os.environ.get('DATABASE_URL') or f    DB_USERNAME = get_env_variable('CLOUD_SQL_USERNAME')
    DB_PASSWORD = get_env_variable('CLOUD_SQL_PASSWORD')
    DB_NAME = get_env_variable('CLOUD_SQL_DATABASE_NAME')
    DB_CONNECTION_NAME = get_env_variable('CLOUD_SQL_CONNECTION_NAME')
    '''