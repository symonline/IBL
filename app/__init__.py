from flask import Flask, render_template, make_response
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate
import sqlite3
import pdfkit

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

migrate=Migrate(app,db)


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
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///right-database.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False


from app import routes, models

if __name__ == '__main__':
     # Create tables
    db.create_all()
    app.run(host='127.0.0.1', port=8000, debug=True)