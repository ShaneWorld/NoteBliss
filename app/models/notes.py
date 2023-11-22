from app.extensions import db
from sqlalchemy import func

class Notes(db.Model):

    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer)
    content = db.Column(db.Text, nullable = False)
    title = db.Column(db.Text, nullable = False)
    html_content = db.Column(db.Text, nullable = False)
    created_at = db.Column(db.DateTime, server_default=func.now())
    
    def __init__(self, user_id, content,title, html_content):
        self.user_id = user_id
        self.content = content
        self.title = title
        self.html_content = html_content