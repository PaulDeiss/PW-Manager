#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

import my_env as env

my_db = SQLAlchemy()
DB_NAME = "database.db"


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = env.SECRET_KEY_FLASK_APP
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    my_db.init_app(app)

    from .views import views
    from .authenticate import auth

    app.register_blueprint(views, url_prefix='views/')
    app.register_blueprint(auth, url_prefix='auth/')

    # from .db_models import User, Note
