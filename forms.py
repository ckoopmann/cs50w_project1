from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    username = StringField("Username",
                    validators = [DataRequired(),Length(min = 2, max = 20)])
    email = StringField("E-Mail", validators = [DataRequired(),Email()])
    password = PasswordField("Password",validators = [DataRequired()])
    confirm_password = PasswordField("Confirm password", validators = [DataRequired(), EqualTo("password")])
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    username = StringField("username",
                    validators = [DataRequired(),Length(min = 2, max = 20)])
    password = PasswordField("password",validators = [DataRequired()])
    remember = BooleanField("remember me")
    submit = SubmitField("Login")
