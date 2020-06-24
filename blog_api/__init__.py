
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)


app.config.from_object(Config)
db = SQLAlchemy(app)
bcryt = Bcrypt(app)
migrate=Migrate(app,db)
login_manager =LoginManager()

from . import routes