from flask import Blueprint, render_template, redirect, url_for, flash
from car_inventory.db import db
from car_inventory.auth.forms import SignUpForm
from car_inventory.auth.models import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(first_name=form.first_name.data, last_name=form.last_name.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Account created successfully!', 'success')
        return redirect(url_for('auth.login'))
    return render_template('signup.html', form=form)

@auth_bp.route('/login')
def login():
    return render_template('login.html')
