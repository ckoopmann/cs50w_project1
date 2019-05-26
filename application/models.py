from application import db, login_manager
from flask_login import UserMixin
from application import db

@login_manager.user_loader
def load_user(user_id):
    user_data = db.session.execute("SELECT * FROM user where id = :user_id", {"user_id": user_id}).fetchone()
    return User(int(user_id))

class User( UserMixin):
    def __init__(self, id):
        self.id = id

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
