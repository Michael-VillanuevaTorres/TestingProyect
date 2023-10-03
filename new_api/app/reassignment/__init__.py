from flask import Blueprint

bp = Blueprint('admin', __name__)

from app.reassignment import routes