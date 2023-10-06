from app.user import bp as app
from app.extensions import db

from app.utils import report_to_list, product_to_list, developer_to_list

from flask import jsonify, request

from app.models.developer import Developer

@app.route('/reports', methods=['GET'])
def get_actives_reports_from_developer():
    id_dev = request.args.get('id_dev')
    developer = Developer.query.filer_by(id=id_dev).first()
    
    if developer is None:
        return jsonify({'message': 'el desarollador no existe'}), 400
    
    reports = Developer.query.filter_by(id=id_dev).all()
    reports = [report for report in reports if report.id_state != 3]

    reports_json = [report_to_list(report) for report in reports]
    
    return jsonify(reports_json), 200

@app.route('number/product/reports/all', methods=['GET'])
def get_number_of_total_reports_and_reports_related_to_product_from_developer():
    pass

@app.route('/product/reports/all', methods=['GET'])
def get_all_reports_from_products_related_to_developer():
    pass

@app.route('/get', methods=['GET'])
def get_developer():
    id_dev = request.args.get('id_dev')
    developer = Developer.query.filer_by(id=id_dev).first()

    if developer is None:
        return jsonify({'message': 'el desarollador no existe'}), 400
    
    developer_json = [developer_to_list(developer)]
    return jsonify(developer_json)