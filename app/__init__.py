from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_utils import database_exists, create_database
from flask_migrate import Migrate

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

if not database_exists(db.engine.url):
    create_database(db.engine.url)

migrate  = Migrate(app, db)

from .models import *
from .routes import *