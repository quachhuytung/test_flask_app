from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config import Config

app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)
print(db.engine.url)

result = db.engine.execute("select 1;")
for r in result:
    print(r[0])


from .routes import *