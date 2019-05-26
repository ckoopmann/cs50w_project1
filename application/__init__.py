from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

app = Flask(__name__)
app.config["SECRET_KEY"] = "f469800586e8f8869d7557372176c794"
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://igebfuidzqsctq:0feaad99b38613562d4a4f3ce1fdda2f668e845cd274c45b75f0024170f2221f@ec2-54-75-238-138.eu-west-1.compute.amazonaws.com:5432/d5a2jrhp1v74ts'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

db.session.execute('CREATE TABLE IF NOT EXISTS users (id SERIAL PRIMARY KEY, username VARCHAR(20), email VARCHAR(120), password VARCHAR(60));')
db.session.commit()

from application import routes
