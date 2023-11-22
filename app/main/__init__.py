from flask import Blueprint

bp1 = Blueprint('main', __name__)

from app.main import routes
