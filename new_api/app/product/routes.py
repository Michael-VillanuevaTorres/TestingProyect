from app.product import bp as app
from app.extensions import db
from app.utils import report_to_list, product_to_list, developer_to_list

from app.models.product import Product
from app.models.report import Report
from app.models.relationship_developer_product import RelationshipDeveloperProduct
from app.models.developer import Developer

from flask import jsonify, request

@app.route('/get', methods=['GET'])
def get_single_product():
    id_product = request.args.get('id_product')
    product = Product.query.get(id_product)
    
    if product is None:
        return jsonify({'message': 'el producto no existe'}), 400
    
    product_json = product_to_list(product)
    
    return jsonify(product_json), 200

def get_product(id_product):
    product = Product.query.get(id_product)
    
    if product is None:
        return 

@app.route('/get/all', methods=['GET'])
def get_all_products():
    products = Product.query.all()
    
    if len(products) == 0:
        return jsonify({'message': 'no hay productos'}), 400

    products_json = [product_to_list(product) for product in products]

    return jsonify(products_json), 200

@app.route('/get/pending_reports', methods=['GET'])
def get_pending_reports():
    id_product = request.args.get('id_product')
    
    if Product.query.get(id_product) is None:
        return jsonify({'message': 'el producto no existe'}), 400
    
    reports = get_pending_reports(id_product)
    
    if len(reports) == 0:
        return jsonify({'message': 'el producto no tiene reportes pendientes'}), 400
    
    reports_json = [report_to_list(report) for report in reports]

    return jsonify(reports_json), 200

def get_pending_reports(id_product):
    return Report.query.filter_by(id_product=id_product, id_state=0).all()

@app.route('/get/reports/all', methods=['GET'])
def get_all_reports_from_product():
    id_product = request.args.get('id_product')
    
    if Product.query.get(id_product) is None:
        return jsonify({'message': 'el producto no existe'}), 400
    
    reports = Report.query.filter_by(id_product=id_product).all()

    if len(reports) == 0:
        return jsonify({'message': 'el producto no tiene reportes asignados'}), 400
    
    #create a json with the information of the reports'
    reports_json = [report_to_list(report) for report in reports]  
      
    return jsonify(reports_json), 200  

@app.route('/get/developers/all', methods=['GET'])
def get_developers_from_product():
    id_product = request.args.get('id_product')
    

    if Product.query.get(id_product) is None:
        return jsonify({'message': 'el producto no existe'}), 400
    
    relationship = RelationshipDeveloperProduct.query.filter_by(id_product=id_product).all()
    
    if len(relationship) == 0:
        return jsonify({'message': 'el producto no tiene desarrolladores asignados'}), 400

    
    developers = []
    for developer in relationship:
        developers.append(Developer.query.get(developer.id_developer))
    
    developers_jsons = [developer_to_list(developer) for developer in developers]
    return jsonify(developers_jsons), 200

def add_product(name):
    product = db.product(name)
    db.session.add(product)
    db.session.commit()

def add_developer_product(id_developer, id_product):
    developer_product = db.developer_product(id_developer, id_product)
    db.session.add(developer_product)
    db.session.commit()
