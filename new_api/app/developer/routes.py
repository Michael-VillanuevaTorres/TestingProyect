from app.user import bp as app
from app.extensions import db

from flask import jsonify, request

@app.route('/reports', methods=['GET'])
def get_actives_reports_from_developer():
    pass

@app.route('number/product/reports/all', methods=['GET'])
def get_number_of_total_reports_and_reports_related_to_product_from_developer():
    pass

@app.route('/product/reports/all', methods=['GET'])
def get_all_reports_from_products_related_to_developer():
    pass

@app.route('/get', methods=['GET'])
def get_developer():
    pass    
