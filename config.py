import os

class Config(object):
    
    #@classmethod
    
    
    # def get_env_variable(cls, name):
        # try:
            # return os.environ.get(name)
        # except KeyError:
            # message = f"Expected environment variable '{name}' not set."
            # raise Exception(message)
    
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    DEBUG = os.environ.get('DEBUG')
    HOST = os.environ.get('HOST')
    DATABASE_URI ='postgres://oholkjlekcyeki:5ce0c19497d9f781f6c1d1a172444d1e861fed1a8f5a7bc7aea2b00cfd5548cc@ec2-174-129-214-193.compute-1.amazonaws.com:5432/derf5i0bvu168'
    
    '''
     os.environ.get('DATABASE_URL') or f    DB_USERNAME = get_env_variable('CLOUD_SQL_USERNAME')
    DB_PASSWORD = get_env_variable('CLOUD_SQL_PASSWORD')
    DB_NAME = get_env_variable('CLOUD_SQL_DATABASE_NAME')
    DB_CONNECTION_NAME = get_env_variable('CLOUD_SQL_CONNECTION_NAME')
    '''