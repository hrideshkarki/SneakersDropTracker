from flask import Flask
from config import Config
from .models import db, User
from flask_migrate import Migrate
from .api import api
from flask_cors import CORS
# from flask_moment import Moment

app = Flask(__name__)
app.config.from_object(Config)
cors = CORS()


db.init_app(app)
migrate = Migrate(app,db)
cors.init_app(app)

app.register_blueprint(api)

from . import routes
from . import models