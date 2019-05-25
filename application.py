import os

from flask import Flask, session, render_template, url_for, flash, redirect, get_flashed_messages
from flask_session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config["SECRET_KEY"] = "f469800586e8f8869d7557372176c794"

# Check for environment variable
if not os.getenv("DATABASE_URL"):
    raise RuntimeError("DATABASE_URL is not set")

# Configure session to use filesystem
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Set up database
engine = create_engine(os.getenv("DATABASE_URL"))
db = scoped_session(sessionmaker(bind=engine))


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

if __name__ == "__main__":
    app.run(debug = 1)
