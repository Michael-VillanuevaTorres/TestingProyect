from app.user import bp as app
from app.extensions import db

from flask import jsonify, request

@app.route('/likes', methods=['GET'])
def get_likes_from_user():
    pass

@app.route('/reports', methods=['GET'])
def get_reports_from_user():
    pass  
