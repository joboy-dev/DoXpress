import os

from flask import Flask, render_template, request, redirect, typing as ft, url_for, flash, abort
from flask_wtf.csrf import CSRFProtect
from flask.views import View
from flask_login import LoginManager, login_required, login_url, logout_user, login_user, current_user

from werkzeug.security import generate_password_hash, check_password_hash
from whitenoise import WhiteNoise

from pathlib import Path
from dotenv import load_dotenv

from datetime import datetime
import time

from models import db, User, Todo
from wtf_forms.user_forms import LoginForm, SignUpForm
from wtf_forms.todo_forms import AddTodoForm, EditTodoForm
from wtf_forms.password_validator import is_valid_password

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR, ".env"))

app = Flask(__name__)
app.secret_key = os.getenv('FLASK_SECRET_KEY')

# configure csrf protection for forms
csrf = CSRFProtect(app)

# setting up flask login manager
login_manager = LoginManager()
login_manager.init_app(app)

# configuring whitenoise for static files
app.wsgi_app = WhiteNoise(app.wsgi_app, root='static/')

# configuring database
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/doxpress_db'
db.init_app(app)

# create all tables
with app.app_context():
    db.create_all()

session = db.session

# login manager config
@login_manager.user_loader
def load_user(user_id):
    return session.query(User).get(str(user_id))

# Copyright year
year = datetime.now().year
