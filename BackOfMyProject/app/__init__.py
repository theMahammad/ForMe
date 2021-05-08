from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
db = SQLAlchemy(app)
# IKISI DE EYNI SHEY
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///data.db'

from admin.routes import *


from main.routes import *
from app.models import *
