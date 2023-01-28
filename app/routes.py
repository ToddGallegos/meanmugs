from app import app
from flask import render_template, request, redirect, url_for, flash
from .models import User, Mugs
from flask_login import current_user, login_required
import requests
import os
from .auth.forms import AddMugsForm

@app.route('/', methods=["GET", "POST"])
def mugs():
    mugs = Mugs.query.all()
    form = AddMugsForm()
    if request.method == "POST":
        if form.validate():
            title = form.title.data
            img_url = form.img_url.data
            caption = form.caption.data
            price = form.price.data
            quantity = form.quantity.data
            
            mug = Mugs(title, img_url, caption, price, quantity)
            mug.saveToDB()
            mugs = Mugs.query.all()
            flash("I THINK YOU CREATED A MUG")
            for i in range(len(mugs)):
                mugs[i].deleteFromDB()
            return render_template('mugs.html', form = form, mugs = mugs)
        else:
            mugs = Mugs.query.all()
            flash("Invalid input. Please try again.")
            return render_template('mugs.html', form = form, mugs=mugs)
    
    elif request.method == "GET":
        return render_template('mugs.html', form = form, mugs=mugs)
