from flask import Flask
from flask_login import LoginManager

app = Flask(__name__)
login_manager = LoginManager()

app.config['WTF_CSRF_ENABLED'] = False

from .models import db, User, Student, Teacher
import api.users
import api.students
import api.teachers