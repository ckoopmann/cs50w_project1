from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import User

class RegistrationForm(FlaskForm):
    username = StringField("Username",
                    validators = [DataRequired(),Length(min = 2, max = 20)])
    email = StringField("E-Mail", validators = [DataRequired(),Email()])
    password = PasswordField("Password",validators = [DataRequired()])
    confirm_password = PasswordField("Confirm password", validators = [DataRequired(), EqualTo("password")])
    submit = SubmitField("Register")

    def validate_username(self, username):
        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError(f'Username {username.data} already exists!')

    def validate_email(self, email):
        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError(f'Email {email.data} already in use!')



class LoginForm(FlaskForm):
    username = StringField("username",
                    validators = [DataRequired(),Length(min = 2, max = 20)])
    password = PasswordField("password",validators = [DataRequired()])
    remember = BooleanField("remember me")
    submit = SubmitField("Login")
