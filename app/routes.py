from app import app
from flask import render_template, request, redirect, url_for, flash, session
from .models import Cart, User, Mugs
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


@app.route("/cart")
def cart():
    user_id = current_user.id
    cart_items = Cart.query.filter_by(user_id=user_id).all()
    mugs = []
    for item in cart_items:
        mug = Mugs.query.get(item.mug_id)
        mug.quantity = item.quantity
        mugs.append(mug)
    return render_template('cart.html', cart=mugs)

@app.route('/<int:mug_id>/add_to_cart', methods=["POST", "GET"])
def add_to_cart(mug_id):
    mug = Mugs.query.get(mug_id)

    if current_user.is_authenticated:
        user_id = current_user.id
        cart_item = Cart.query.filter_by(mug_id=mug_id, user_id=user_id).first()
        if cart_item:
            cart_item.quantity += 1
            cart_item.saveToDB()
        else:
            cart = Cart(mug_id=mug_id, user_id=user_id, quantity=1)
            cart.saveToDB()
    else:
        flash('You need to log in to add items to your cart', category='danger')
        return redirect(url_for('auth.loginPage'))
    return redirect(url_for('cart'))

@app.route('/cart/<int:mug_id>/remove', methods=["POST", "GET"])
def remove_from_cart(mug_id):
    user_id = current_user.id
    cart_item = Cart.query.filter_by(mug_id=mug_id, user_id=user_id).first()

    if not cart_item:
        return redirect(url_for('cart'))

    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.saveToDB()
    else:
        cart_item.deleteFromDB()

    return redirect(url_for('cart'))

@app.route('/cart/clear', methods=["POST", "GET"])
def clear_cart():
    user_id = current_user.id
    cart_items = Cart.query.filter_by(user_id=user_id).all()

    for cart_item in cart_items:
        cart_item.deleteFromDB()

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