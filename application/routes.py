from application import app, db, bcrypt
from application.forms import RegistrationForm, LoginForm
from flask import render_template, url_for, flash, redirect, get_flashed_messages
from application.models import User
from flask_login import login_user, current_user, logout_user

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/registration", methods = ['GET','POST'])
def registration():

    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        db.session.execute("INSERT INTO user(username, email, password) VALUES (:username, :email, :password)",
        {"username":form.username.data, "email":form.email.data, "password":hashed_password})
        flash(f"Account has been created", "success")
        db.session.commit()
        return redirect(url_for("login"))

    return render_template('registration.html', form = form, title = "Registration")


@app.route("/login", methods = ['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember = form.remember.data)
            return redirect(url_for('index'))

        flash('Login failed try again', 'warning')

    return render_template('login.html', form = form)


@app.route("/logout", methods = ['GET'])
def logout():
    logout_user()
    return redirect(url_for('login'))
