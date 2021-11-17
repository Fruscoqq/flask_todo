from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_assets import Environment, Bundle
import os

app = Flask(__name__)
assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle('styles/style.scss', filters='pyscss', output='styles/style.css')
assets.register('scss_all', scss)

app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")

db = SQLAlchemy(app)

from application import routes