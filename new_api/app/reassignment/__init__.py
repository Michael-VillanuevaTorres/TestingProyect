from flask import Blueprint

bp = Blueprint('reassignment', __name__)

from app.reassignment import routes