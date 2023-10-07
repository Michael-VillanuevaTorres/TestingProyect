from flask import Blueprint

bp = Blueprint('developer', __name__)

from app.user import routes