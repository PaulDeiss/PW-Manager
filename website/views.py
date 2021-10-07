#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user

from .db_models import Note
from . import my_db


views = Blueprint('views', __name__)


# @login_required
@views.route('/', methods=['GET', 'POST'])
def home():
    pass


@views.route('/delete-note', methods=['POST'])
def delete_note():
    pass
