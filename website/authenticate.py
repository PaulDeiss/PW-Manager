#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash

from .db_models import User
from . import my_db
"""
import flask
import flask_login

auth = flask.Blueprint('auth', __name__)


@auth.route('/login', methods=['GET', 'POST'])
def login():
    pass


@auth.route('/logout')
@flask_login.login_required
def logout():
    pass


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    pass
