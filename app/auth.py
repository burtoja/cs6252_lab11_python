'''
Created on Mar 25, 2020

@author: CS6252
'''
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash
from . import db
from app.model.user import User

auth = Blueprint('auth', __name__)


@auth.route('/signup')
def signup():
    return render_template('signup.html')


@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    
    user = db.get_user(email)
    if user:
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))
    
    user=User(email, name, generate_password_hash(password, method='sha256'))
    db.add_user(user)
    
    return redirect(url_for('auth.login'))


@auth.route('/login')
def login():
    return render_template('login.html')


@auth.route('/login', method=['POST'])
def login_post():
    return redirect(url_for('main.profile'))

@auth.route('/logout')
def logout():
    return "logout"