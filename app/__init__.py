from flask import Flask
import os
from flask_debugtoolbar import DebugToolbarExtension
import logging
# from app.config import Config

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
print('basedir2: ' + BASE_DIR)
logging.warning("Hello:")

toolbar = DebugToolbarExtension(app)

from app import routes
