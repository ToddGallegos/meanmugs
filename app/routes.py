from app import app
from flask import render_template, request, redirect, url_for
from .models import User, Mugs
from flask_login import current_user, login_required
import requests
import os

@app.route('/')
def mugs():
    return render_template('mugs.html')