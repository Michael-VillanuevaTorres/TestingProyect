from app.developer import bp as app
from app.extensions import db

from app.utils import report_to_list, product_to_list, developer_to_list

from flask import jsonify, request

from app.models.developer import Developer
from app.models.product import Product
from app.models.report import Report

@app.route('/reports', methods=['GET'])
def get_actives_reports_from_developer():
    id_dev = request.args.get('id_dev')
    developer = Developer.query.filter_by(id=id_dev).first()
    
    if developer is None:
        return jsonify({'message': 'el desarollador no existe'}), 400
    
    reports = Report.query.filter_by(id=id_dev).all()
    reports = [report for report in reports if report.id_state != 3]

    reports_json = [report_to_list(report) for report in reports]
    
    return jsonify(reports_json), 200

@app.route('number/product/reports/all', methods=['GET'])
def get_number_of_total_reports_and_reports_related_to_product_from_developer():
    id_dev = request.args.get('id_dev')
    id_product = int(request.args.get('id_product'))
    developer = Developer.query.filter_by(id=id_dev).first()
    if developer is None:
        return jsonify({'message': 'el desarollador no existe'}), 400
    product = Product.query.filter_by(id=id_product).first()
    if product is None:
        return jsonify({'message': 'el producto no existe'})
    #get all the number of total reports where the id_dev is the same as the id_dev in the request and if the state is not 0 or 3
    total_reports = len([report for report in Report.query.filter_by(id_developer=id_dev).all() if report.id_state != 0 and report.id_state != 3])
    #now get the number of total reports where the id_dev is the same as the id_dev in the request and if the state is 3 and the id_product is the same as the id_product in the request
    product_reports = len([report for report in Report.query.filter_by(id_developer=id_dev).all() if report.id_state != 0 and report.id_state != 3 and report.id_product == id_product])   
    #create a json with the information of the reportes
    reports = {'total_reports': total_reports, 'product_reports': product_reports}
    #return the json
    return jsonify(reports)

@app.route('/product/reports/all', methods=['GET'])
def get_all_reports_from_products_related_to_developer():
    id_dev = request.args.get('id_dev')
    developer = Developer.query.filter_by(id=id_dev).first()
    
    if developer is None:
        return jsonify({'message': 'el desarollador no existe'}), 400
    
    #get from Developer table, all the products where the id_dev is the same as the id_dev in the request
    products = Product.query.filter_by(id_developer=id_dev).all()
    #create a list with the id_product from the products
    id_products = [product.id_product for product in products]
    #get all the reports where the id_product is in the id_products list
    reports = Report.query.filter(Report.id_product.in_(id_products)).all()
    #create a json with the information of the reports
    reports_json = [report_to_list(reports)]
    #return the json
    return jsonify(reports_json), 200

@app.route('/get', methods=['GET'])
def get_developer():
    id_dev = request.args.get('id_dev')
    developer = Developer.query.filer_by(id=id_dev).first()

    if developer is None:
        return jsonify({'message': 'el desarollador no existe'}), 400
    
    developer_json = [developer_to_list(developer)]
    return jsonify(developer_json)