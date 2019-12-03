from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate
import sqlite3
# import psycopg2
import os


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

migrate=Migrate(app,db)

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

# db_url = f'/cloudsql/{Config.DATABASE_URL}'   google cloud sql
DB_URL = os.environ.get('DATABASE_URL') # or Config.DATABASE_URL 
# DB_URL = f'postgresql+psycopg2://{db_user}:{db_password}@{db_url}/{db_name}' google cloud sql

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URL or os.environ.get('DATABASE_URL_LOC') # 'sqlite:///right-database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY') 

from app import routes, models

if __name__ == '__main__':
     # Create tables
    db.create_all()
    app.run(host='127.0.0.1', port=5000, debug=True)

