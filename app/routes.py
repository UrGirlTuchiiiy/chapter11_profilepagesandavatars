from app import app, db
from app.models import User
from flask_login import login_user, logout_user, login_required
from flask import render_template, flash, redirect, url_for
from app.forms import RegisterForm, LoginForm


@app.route('/')
@app.route('/home')
@login_required
def index():
    """Index URL"""
    return render_template('index.html', title='Index Page')

@app.route('/logout')
def logout():
    """Logout URL"""
    logout_user()
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    """Login URL"""
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        flash(f'Welcome back {form.username.data}!')
        return redirect(url_for('index'))
    return render_template('login.html', title='Login Page', form=form)
    
@app.route('/register', methods=['GET', 'POST'])
def register():
    """Register URL"""
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'You have been registered {form.username.data}')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register Page', form=form)

@app.route('/addproduct', methods=['GET', 'POST'])
@login_required
def addproduct():
    """Addproduct URL"""
    form = AddproductForm()
    if form.validate_on_submit():
        flash(f'Your product has been saved')
        return redirect(url_for('index'))
    return render_template('addproduct.html', title='Add_Product', form=form)
    