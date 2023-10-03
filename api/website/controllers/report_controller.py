from .. import db
from flask import Blueprint, jsonify, request

report_controller = Blueprint('report_controller', __name__)

@report_controller.route('/reports/comments', methods=['POST'])
def add_comment():
    data = request.json
    id_report = request.args.get('id_report')
    
    if db.reporte.query.filter_by(id=id_report).first() is None:
        return jsonify({'message': 'The id_report is not in the database'}), 400
    
    if data.get('text') is None:
        return jsonify({'message': 'Comment not added. Text is needed'}), 400
    
    commit_comment(data['text'], id_report)
    
    return jsonify({'message': 'Comment added successfully.'}), 201

def commit_comment(description, id_report):
    comentario = db.comentario(description, id_report)
    db.session.add(comentario)
    db.session.commit()

@report_controller.route('/reports/like', methods=['POST'])
def add_like():
    id_report = request.args.get('id_report')
    id_user = request.args.get('id_user')
    
    report = db.reporte.query.get_or_404(id_report)
    
    if db.like.query.filter_by(id_desarrollador=id_user, id_reporte=id_report).first() is not None:
        return jsonify({'message': 'The like is already in the database'}), 400
    
    commit_like(id_user, id_report)
    report.add_likes(1)

    return jsonify({'message': 'like added successfully.'}), 201

def commit_like(id_user, id_reporte):
    like = db.like(id_user,id_reporte)
    db.session.add(like)
    db.session.commit()

@report_controller.route('/reports/add', methods=['POST'])
def add_report():
    data = request.json
    id_product = request.args.get('id_product')
    id_cliente = request.args.get('id_cliente')
    
    if db.producto.query.filter_by(id=id_product).first() is None:
        return jsonify({'message': 'The id_product is not in the database'}), 400
    
    if data.get('title') is None:
        return jsonify({'message': 'Report not added. Title is needed'}), 400
    
    if data.get('description') is None:
        return jsonify({'message': 'Report not added. Description is needed'}), 400
    
    commit_report(data['title'], data['description'], id_product, id_cliente)
    
    return jsonify({'message': 'Report added successfully.'}), 201

def commit_report(titulo,descripcion,id_producto,id_cliente):
    reporte = db.reporte(titulo, descripcion, id_producto,id_cliente)
    db.session.add(reporte)
    db.session.commit()

@report_controller.route('/comments/get', methods=['GET'])
def get_comments():
    id_report = request.args.get('id_report')

    if db.reporte.query.filter_by(id=id_report).first() is None:
        return jsonify({'message': 'The id_report is not in the database'}), 400

    comments = db.comentario.query.filter_by(id_reporte=id_report).all()
    comments_json = [object_to_list_comment(comment) for comment in comments]

    return jsonify(comments_json), 200

def object_to_list_comment(comment):
    comment_json = {
        'id': comment.id,
        'contenido': comment.contenido,
        'date': comment.fecha
    }
    return comment_json

@report_controller.route('/reports/get', methods=['GET'])
def get_report():
    quantity = request.args.get('quantity')
    id_product = request.args.get('id_product')

    if db.producto.query.filter_by(id=id_product).first() is None:
        return jsonify({'message': 'The id_product is not in the database'}), 400

    if quantity is None:
        return jsonify({'message': 'Quantity not specified'}), 400

    if int(quantity) > db.reporte.query.filter_by(id_producto=id_product).count():
        return jsonify({
            'message': f'The quantity is bigger than the number of reports. Quantity asked is: {quantity} The number of reports with the product id is: {db.reporte.query.filter_by(id_producto=id_product).count()}'
        }), 400

    reports = db.reporte.query.filter_by(id_producto=id_product).order_by(db.reporte.likes.desc()).limit(quantity).all()
    reports_json = [object_to_list_report(report) for report in reports]

    return jsonify(reports_json), 200

@report_controller.route('/reports/all', methods=['GET'])
def get_all_reports():
    reports = db.reporte.query.all()
    reports_json = [object_to_list_report(report) for report in reports]

    return jsonify(reports_json), 200

@report_controller.route('/reports/all/product/', methods=['GET'])
def get_all_reports_from_a_specific_product():
    id_product = request.args.get('id_product')
    if db.producto.query.filter_by(id=id_product).first() == None:
        return jsonify({'message': 'The id_product is not in the database'}), 400
    reports = db.reporte.query.filter_by(id_producto=id_product).all()
    #revisar si se quiere asi o que solamente entregue una lista vacia
    if len(reports) == 0:
        return jsonify({'message': 'There are no reports with that id_product'}), 400
    
    reports_json = [object_to_list_report(report) for report in reports]
    
    return jsonify(reports_json), 200

@report_controller.route('/report/get', methods=['GET'])
def get_single_report():
    id_report = request.args.get('id_report')
    report = db.reporte.query.get_or_404(id_report)
    
    report_json = [object_to_list_report(report) for report in report]
    
    return jsonify(report_json), 200

def object_to_list_report(report):
    report_json = {
        'id': report.id,
        'title': report.titulo,
        'description': report.descripcion,
        'likes': report.likes,
        'date': report.fecha,
        'id_producto': report.id_producto,
        'id_prioridad': report.id_prioridad,
        'id_estado': report.id_estado,
        'id_developer': report.id_developer
    }
    return report_json

@report_controller.route('/reports/update/estado', methods=['POST'])
def update_estado():
    id_report = request.args.get('id_report')
    id_estado = request.args.get('id_estado')
    
    if db.reporte.query.filter_by(id=id_report).first() == None:
        return jsonify({'message': 'The id_report is not in the database'}), 400
    if db.estado.query.filter_by(id=id_estado).first() == None:
        return jsonify({'message': 'The id_estado is not in the database'}), 400
    
    report = db.reporte.query.get_or_404(id_report)
    report.id_estado = id_estado
    db.session.commit()
    
    return jsonify({'message': 'Estado updated successfully.'}), 201
    

@report_controller.route('/reports/update/prioridad', methods=['POST'])
def update_prioridad():
    id_report = request.args.get('id_report')
    id_prioridad = request.args.get('id_prioridad')
    
    if db.reporte.query.filter_by(id=id_report).first() == None:
        return jsonify({'message': 'The id_report is not in the database'}), 400
    if db.prioridad.query.filter_by(id=id_prioridad).first() == None:
        return jsonify({'message': 'The id_estado is not in the database'}), 400
    
    report = db.reporte.query.get_or_404(id_report)
    report.id_prioridad = id_prioridad
    db.session.commit()
    
    return jsonify({'message': 'Estado updated successfully.'}), 201

@report_controller.route('/reports/check/estados', methods=['GET'])
def check_estados():
    id_report= request.args.get('id_report')
    
    if db.reporte.query.filter_by(id=id_report).first() == None:
        return jsonify({'message': 'The id_report is not in the database'}), 400
    #return all the estados, but the id=0 and the current id_estado
    estados = db.estado.query.filter(db.estado.id != 0).filter(db.estado.id != db.reporte.query.get_or_404(id_report).id_estado).all()
    estados_json = []
    for estado in estados:
        estados_json.append(object_to_list_estado(estado))
        
    return jsonify(estados_json), 200

def object_to_list_estado(estado):
    estado_json = {}
    estado_json['id'] = estado.id
    estado_json['nombre'] = estado.nombre
    
    return estado_json

@report_controller.route('/reports/estados/all', methods=['GET'])
def all_estados():
    #return all the estados
    estados = db.estado.query.all()
    estados_json = []
    
    for estado in estados:
        estados_json.append(object_to_list_estado(estado))
        
    return jsonify(estados_json), 200

@report_controller.route('/reports/add/developer/', methods=['POST'])
def add_developer():
    id_report = request.args.get('id_report')
    id_developer = request.args.get('id_dev')
    
    if db.reporte.query.filter_by(id=id_report).first() is None:
        return jsonify({'message': 'The id_report is not in the database'}), 400
    if db.desarrollador.query.filter_by(id=id_developer).first() is None:
        return jsonify({'message': 'The id_developer is not in the database'}), 400
    
    report = db.reporte.query.get_or_404(id_report)
    commit_developer(report, id_developer)
    
    return jsonify({'message': 'Developer added successfully.'}), 201

def commit_developer(report, id_developer):
    report.id_developer = id_developer
    report.id_estado = 1
    db.session.commit()

@report_controller.route('/reports/prioridad/all', methods=['GET'])
def all_prioridad():
    #return all the estados
    prioridades = db.prioridad.query.all()
    prioridades_json = [object_to_list_prioridad(prioridad) for prioridad in prioridades]
        
    return jsonify(prioridades_json), 200

def object_to_list_prioridad(prioridad):
    prioridad_json = {
        'id': prioridad.id,
        'nombre': prioridad.nombre
    }
    return prioridad_json

def add_desarrollador_producto(id_desarrollador, id_producto):
    desarrollador_producto = db.desarrollador_producto(id_desarrollador, id_producto)
    db.session.add(desarrollador_producto)
    db.session.commit()

def add_estado(nombre):
    estado = db.estado(nombre)
    db.session.add(estado)
    db.session.commit()

def add_producto(nombre):
    producto = db.producto(nombre)
    db.session.add(producto)
    db.session.commit()