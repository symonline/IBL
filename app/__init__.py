from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate=Migrate(app,db)


'''
ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://apvest_admin:Symbolo2@@localhost/apvest_db'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''
    '''
    
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://apvest_admin:Symbolo2@@localhost/apvest_db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False


from app import routes, models

if __name__ == '__main__':
     # Create tables
    #db.create_all()
    
    app.run(host='127.0.0.1', port=8000, debug=True)