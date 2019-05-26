from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config["SECRET_KEY"] = "f469800586e8f8869d7557372176c794"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

db.session.execute('CREATE TABLE IF NOT EXISTS user(id SERIAL PRIMARY KEY, username VARCHAR(20), email VARCHAR(120), password VARCHAR(60));')
db.session.commit()

from application import routes
