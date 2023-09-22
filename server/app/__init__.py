from flask import Flask
from flask_login import LoginManager
from .models import db
from os import path
import sys

sys.dont_write_bytecode = True

DB_NAME = 'database.db'

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'anton'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'

    db.init_app(app)

    from app.api import views
    from app.authentication import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    login_manager = LoginManager()
    login_manager.init_app(app)

    from .models import User, Task

    initialize_database(app)

    return app

def initialize_database(app):
    if not path.exists("server/" + DB_NAME):
        try:
            with app.app_context():
                db.create_all()
                print("Created database!")
        except Exception as e:
            print("> Error: DBMS Exception: " + str(e))

