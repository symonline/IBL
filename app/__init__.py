from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
# from flask_migrate import Migrate
import sqlite3
# import psycopg2
import os


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy() 
db.init_app(app)

# from manage import migrate, manager


'''
ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://right-db:Symbolo2@@localhost/right-database'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''
    '''
    
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://apvest_admin:Symbolo2@@localhost/apvest_db'
''' google cloud sql
db_name = Config.DB_NAME
db_user = Config.DB_USERNAME
db_password = Config.DB_PASSWORD
connection_name = Config.DB_CONNECTION_NAME
'''
# db_url = f'/cloudsql/{Config.DATABASE_URL}'   google cloud sql
app.config['DATABASE_URI'] = os.environ.get('DATABASE_URL')
# DB_URL = f'postgresql+psycopg2://{db_user}:{db_password}@{db_url}/{db_name}' google cloud sql

# app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL or 'sqlite:///right-database.sqlite3' 
#app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False


from app import routes, models

if __name__ == '__main__':
     # Create tables
    db.create_all()
    app.run(debug=True)
