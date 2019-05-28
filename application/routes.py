from application import app, db, bcrypt
from application.forms import RegistrationForm, LoginForm, SearchForm, ReviewForm
from flask import render_template, url_for, flash, redirect, get_flashed_messages
from application.models import User
from flask import request
from flask_login import login_user, current_user, logout_user

@app.route("/", methods = ['GET','POST'])
def index():
    if not current_user.is_authenticated:
        return redirect(url_for('registration'))

    form = SearchForm()
    if request.method == 'POST':
        author = "%"  if form.author.data is None else "%"+form.author.data+"%"
        title = "%" if form.title.data is None else "%"+form.title.data+"%"
        isbn =  "%" if form.isbn.data is None else "%"+form.isbn.data+"%"
        results = db.session.execute("SELECT * FROM books WHERE author LIKE :author AND title LIKE :title AND isbn LIKE :isbn", {"author":author, "title":title, "isbn":isbn})
        return render_template("index.html", form = form, results =         results.fetchall())

    return render_template("index.html", form = form)

@app.route("/registration", methods = ['GET','POST'])
def registration():

    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = RegistrationForm()

    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        db.session.execute("INSERT INTO users(username, email, password) VALUES (:username, :email, :password)",
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
        user_data = db.session.execute("SELECT * FROM users where username = :username", {"username": form.username.data}).fetchone()
        if user_data and bcrypt.check_password_hash(user_data.password, form.password.data):
            login_user(User(user_data.id), remember = form.remember.data)
            return redirect(url_for('index'))

        flash('Login failed try again', 'warning')

    return render_template('login.html', form = form)


@app.route("/logout", methods = ['GET'])
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route("/book/<int:id>", methods = ['GET','POST'])
def book(id):
    book = db.session.execute("SELECT * FROM books WHERE id = :id",
    {"id":id}).fetchone()
    form = ReviewForm()

    form.set_id(id)

    if form.validate_on_submit():
        db.session.execute("INSERT INTO reviews(user_id, book_id, rating, comment) VALUES (:user_id, :book_id, :rating, :comment)",
        {"user_id":current_user.get_id(), "book_id":id, "rating":form.rating.data, "comment":form.comment.data})
        db.session.commit()

    return render_template('book.html', id = id, book = book, form = form)
