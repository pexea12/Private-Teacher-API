from flask import Flask

app = Flask(__name__)

app.config['WTF_CSRF_ENABLED'] = False

from .models import db, User
import api.users