from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager


app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

# The bottom import is a workaround to circular imports, a common problem with Flask applications
# You are going to see that the routes module needs to import the app variable defined in this script, so putting one of the reciprocal imports at the bottom avoids the error that results from the mutual references between these two files.
from app import routes, models