from os import environ
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('DATABASE_URL') or 'sqlite:///my_database.db'
app.config['SECRET_KEY'] = 'the random string'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = "True"

db = SQLAlchemy(app)

login = LoginManager(app)
login.init_app(app)
login.login_view = 'login'

import routes, models
#db.create_all()
#db.session.commit()