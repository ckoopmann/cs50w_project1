from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, NumberRange
from application import db


class RegistrationForm(FlaskForm):
    username = StringField("Username",
                    validators = [DataRequired(),Length(min = 2, max = 20)])
    email = StringField("E-Mail", validators = [DataRequired(),Email()])
    password = PasswordField("Password",validators = [DataRequired()])
    confirm_password = PasswordField("Confirm password", validators = [DataRequired(), EqualTo("password")])
    submit = SubmitField("Register")

    def validate_username(self, username):
        user = db.session.execute("SELECT * FROM users where username = :username", {"username": username.data}).fetchone()
        if user:
            raise ValidationError(f'Username {username.data} already exists!')

    def validate_email(self, email):
        user = db.session.execute("SELECT * FROM users where email = :email", {"email": email.data}).fetchone()
        if user:
            raise ValidationError(f'Email {email.data} already in use!')



class LoginForm(FlaskForm):
    username = StringField("username",
                    validators = [DataRequired(),Length(min = 2, max = 20)])
    password = PasswordField("password",validators = [DataRequired()])
    remember = BooleanField("remember me")
    submit = SubmitField("Login")

class SearchForm(FlaskForm):
    isbn = StringField("ISBN")
    author = StringField("Author")
    title = StringField("Title")
    submit = SubmitField("Search")

class ReviewForm(FlaskForm):
    rating = IntegerField('Rating (0-5)', [DataRequired(), NumberRange(min=0, max=5)])
    comment = StringField('Comment', [Length(min = 0, max = 500)])
    submit = SubmitField("Submit")
