from flask_sqlalchemy import SQLAlchemy
from functools import wraps
from flask import session, redirect

# Create db
db = SQLAlchemy()

# Login Required
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function
