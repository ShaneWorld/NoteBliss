from flask import Blueprint

bp2 = Blueprint('auth', __name__)

from app.auth import routes
