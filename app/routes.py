from app import app
from flask import render_template, request, redirect, url_for, flash, session, jsonify
from .models import User, Mugs, Cart
from flask_login import current_user, login_required
import requests
import os
from .auth.forms import AddMugsForm


@app.route('/', methods=["GET", "POST"])
def mugs():
    
    mugs = Mugs.query.all()
    
    return render_template('mugs.html', mugs = mugs)

@app.route('/<int:mug_id>', methods=["GET"])
def getMug(mug_id):
    
    mug = Mugs.query.get(mug_id)
    
    return render_template('singlemug.html', mug=mug)

@app.route('/cart', methods=["GET", "POST"])
def cart():

    if 'cart' not in session:
        session['cart'] = []

    return render_template('cart.html', cart=session['cart'])

@app.route('/<int:mug_id>/add_to_cart', methods=["POST", "GET"])
def add_to_cart(mug_id):
    
    mug = Mugs.query.get(mug_id)
    
    if 'cart' not in session:
        session['cart'] = [] 
    
    mugdict = {
        "id": mug.id,
        "title": mug.title,
        "img_url": mug.img_url,
        "caption": mug.caption,
        "price": mug.price,
        "quantity": mug.quantity
        }  
    
    temp = session['cart']
    temp.append(mugdict)
    session['cart'] = temp
    
    return redirect(url_for('cart'))

@app.route('/cart/<int:mug_id>/remove', methods=["POST", "GET"])
def remove_from_cart(mug_id):
    
    if mug_id not in [mug['id'] for mug in session['cart']]:
        return redirect(url_for('cart'))
    
    session['cart'] = [mug for mug in session['cart'] if mug['id'] != mug_id]
    
    return redirect(url_for('cart'))

@app.route("/<int:mug_id>/delete", methods=["POST", "GET"])
def deleteMug(mug_id):
    
    mug = Mugs.query.get(mug_id)

    mug.deleteFromDB()
    return redirect(url_for('mugs'))

@app.route("/addmugs", methods=["POST", "GET"])
def addMug():

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
            
            flash("Successfully Added Mug to Database!")
            return render_template('addmugs.html', form = form)
        
        else:
            flash("Form didn't pass validation.")
            return render_template('addmugs.html', form = form)
        
    elif request.method == "GET":
        return render_template('addmugs.html', form = form)