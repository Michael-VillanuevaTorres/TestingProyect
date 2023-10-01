import db.database as database
from flask import Blueprint, jsonify, request

user_controller = Blueprint('user_controller', __name__)

db = database.db
app = database.app

## get_id
# return id of the request if there is one, else an error message 
def get_id():
    id = request.args.get('id_dev')
    if id is None:
        return jsonify({'error': 'missing ID parameter in the request'}), 400
    return id

## check_id(*id*)
# return error message if the id isnt in our database, do nothing if all is ok 
def check_exist(id_dev, db_param):
    if database.db_param.query.filter_by(id=id_dev).first() == None:
        return jsonify({'message': 'Required ID dont exist in database'}), 400

## get_reportes_from_dev()
# description
@user_controller.route('/dev/reportes/', methods=['GET'])
def get_reportes_from_dev():
    id_dev=get_id()
    check_exist(id_dev,'desarollador')
    #get all the where in the table reporte the id_dev is the same as the id_dev in the request
    reportes = database.reporte.query.filter_by(id_developer=id_dev).all()
    #if the estado from reporte is equal to 3, then the reporte is closed and should not be shown
    reportes = [reporte for reporte in reportes if reporte.id_estado != 3]
    #create a json with the information of the reportes
    reportes = [{'id': reporte.id, 'title': reporte.titulo, 'description': reporte.descripcion, 'likes': reporte.likes, 'date': reporte.fecha, 'id_estado': reporte.id_estado, 'id_prioridad': reporte.id_prioridad, 'id_producto': reporte.id_producto, 'id_developer' : reporte.id_developer} for reporte in reportes]
    #return the json
    return jsonify(reportes)

## get_likes_from_user()
# description
@user_controller.route('/user/liked/', methods=['GET'])
def get_likes_from_user():
    id_user=get_id()
    check_exist(id_user,'desarollador')
    #get all the where in the table reporte the id_dev is the same as the id_dev in the request
    likes = database.like.query.filter_by(id_desarrollador=id_user).all()
    reportes = []
    for like in likes:
        id_reporte = like.id_reporte
        report = database.reporte.query.get_or_404(id_reporte)
        reportes.append(report)
    reportes = [{'id': reporte.id, 'title': reporte.titulo, 'description': reporte.descripcion, 'likes': reporte.likes, 'date': reporte.fecha, 'id_estado': reporte.id_estado, 'id_prioridad': reporte.id_prioridad, 'id_producto': reporte.id_producto, 'id_developer' : reporte.id_developer} for reporte in reportes]
    #return the json
    return jsonify(reportes)

## get_all_reports_and_products()
# description
@user_controller.route('/dev/all/report-product/', methods=['GET'])
def get_all_reports_and_products():
    id_dev=get_id()
    check_exist(id_dev,'desarollador')
    id_product = int(request.args.get('id_product'))
    check_exist(id_product, 'producto')
    #get all the number of total reports where the id_dev is the same as the id_dev in the request and if the estado is not 0 or 3
    total_reports = len([reporte for reporte in database.reporte.query.filter_by(id_developer=id_dev).all() if reporte.id_estado != 0 and reporte.id_estado != 3])
    #now get the number of total reports where the id_dev is the same as the id_dev in the request and if the estado is 3 and the id_product is the same as the id_product in the request
    product_reports = len([reporte for reporte in database.reporte.query.filter_by(id_developer=id_dev).all() if reporte.id_estado != 0 and reporte.id_estado != 3 and reporte.id_producto == id_product])    
    #create a json with the information of the reportes
    reportes = {'total_reports': total_reports, 'product_reports': product_reports}
    #return the json
    return jsonify(reportes)

## get_all_reports_related_to_products()
# description
@user_controller.route('/dev/all-reportes-related-to-products/', methods=['GET'])
def get_all_reports_related_to_products():
    #first get the dev id
    id_dev=get_id()
    #check if the id_dev is in the database
    check_exist(id_dev, 'desarollador')
    #get from desarrollador_producto table, all the products where the id_dev is the same as the id_dev in the request
    productos = database.desarrollador_producto.query.filter_by(id_desarrollador=id_dev).all()
    #create a list with the id_product from the productos
    id_productos = [producto.id_producto for producto in productos]
    #get all the reports where the id_producto is in the id_productos list
    reportes = database.reporte.query.filter(database.reporte.id_producto.in_(id_productos)).all()
    #create a json with the information of the reportes
    reportes_json = [{'id': reporte.id, 'title': reporte.titulo, 'description': reporte.descripcion, 'likes': reporte.likes, 'date': reporte.fecha, 'id_estado': reporte.id_estado, 'id_prioridad': reporte.id_prioridad, 'id_producto': reporte.id_producto, 'id_developer' : reporte.id_developer} for reporte in reportes]
    #return the json
    return jsonify(reportes_json), 200

## get_dev_info()
# description
@user_controller.route('/dev/info/', methods=['GET'])
def get_dev_info():
    id_dev=get_id()
    check_exist(id_dev, 'desarollador')
    #create a json that returns the information of the developer
    developer_json = {'id': developer.id, 'nombre': developer.nombre, 'email': developer.email, 'id_rol': developer.id_rol}
    return jsonify(developer_json)

## get_user_reports()
# description
@user_controller.route('/user/reports/', methods=['GET'])
def get_user_reports():
    id_user = get_id()
    reportes = database.reporte.query.filter_by(id_cliente=id_user).all()
    reportes_json = [{'id': reporte.id, 'title': reporte.titulo, 'description': reporte.descripcion, 'likes': reporte.likes, 'date': reporte.fecha, 'id_estado': reporte.id_estado, 'id_prioridad': reporte.id_prioridad, 'id_producto': reporte.id_producto, 'id_developer' : reporte.id_developer} for reporte in reportes]
    return jsonify(reportes_json), 200 

## add_desarollador()
# description
async def add_desarrollador(nombre, email, id_rol):
    desarrollador = database.desarrollador(nombre, email, id_rol)
    db.session.add(desarrollador)
    db.session.commit()

## add_cliente()
# description
async def add_cliente(nombre, email):
    cliente = database.cliente(nombre, email)
    db.session.add(cliente)
    db.session.commit()

## add_id_rol()
# description
async def add_id_rol(nombre):
    rol = database.rol(nombre)
    db.session.add(rol)
    db.session.commit()