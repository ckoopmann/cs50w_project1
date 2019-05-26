from application import app
from application.forms import RegistrationForm, LoginForm
from flask import render_template, url_for, flash, redirect, get_flashed_messages

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/registration", methods = ['GET','POST'])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}", "success")
        return redirect(url_for("index"))

    return render_template('registration.html', form = form, title = "Registration")


@app.route("/login", methods = ['GET','POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        flash(f"Account created for {form.username.data}", "success")
        return redirect(url_for("index"))

    return render_template('login.html', form = form)
