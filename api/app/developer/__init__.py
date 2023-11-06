from flask import Blueprint

bp = Blueprint('developer', __name__)

from app.developer import routes