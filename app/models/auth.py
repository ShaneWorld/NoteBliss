from app.extensions import db

class Users(db.Model):

    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(20), unique = True)
    hash = db.Column(db.String(16))
    
    def __init__(self, username, hash):
        self.username = username
        self.hash = hash
