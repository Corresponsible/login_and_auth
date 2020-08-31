from app import app, db, login
from flask import request, render_template, flash, redirect, url_for
from models import User
from forms import RegistrationForm, LoginForm
from werkzeug.urls import url_parse
from flask_login import current_user, login_user, logout_user, login_required

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
  
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        flash("You are already logged in.")
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password_hash(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('user'))
    return render_template('login.html', title='Sign In', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        flash("You need to logout first.")
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash("You are a registered user now! Login into system")
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/')
def index():
    return render_template('landing_page.html')

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))
    
@app.route('/user')
def user():
    return render_template('user.html')