from .. import db
from flask import Blueprint, jsonify, request

encargado_controller = Blueprint('encargado_controller', __name__)

#ENDPOINT API para agregar una solicitud de reasignacion a la BD
@encargado_controller.route('/reasignacion/add/', methods=['POST'])
def add_reasingation_petition():
    data = request.json
    id_report = request.args.get('id_report')
    id_developer = request.args.get('id_developer')
    # Validaciones y manejo de errores
    result = add_solicitud_reasignacion(id_report, id_developer, data['motivo'])
    if result['success']:
        db.session.commit()
        return jsonify({'message': 'Solicitud de reasignacion agregada exitosamente.'}), 201
    else:
        return jsonify({'message': result['message']}), 400

def add_solicitud_reasignacion(id_report, id_developer, motivo):
    if not db.reporte.query.filter_by(id=id_report).first():
        return {'success': False, 'message': 'The id_report is not in the database'}

    if not db.desarrollador.query.filter_by(id=id_developer).first():
        return {'success': False, 'message': 'The id_dev is not in the database'}

    if db.solicitud_reasignacion.query.filter_by(id_dev=id_developer, id_reporte=id_report).first():
        return {'success': False, 'message': 'The id_dev is already in the database'}

    reasignation = db.solicitud_reasignacion(id_report, id_developer, motivo)
    db.session.add(reasignation)
    return {'success': True}  


@encargado_controller.route('/reasignacion/delete/', methods=['DELETE'])
def delete_reasingation_petition():
    id_report = request.args.get('id_report')
    id_dev = request.args.get('id_dev')
    
    delete_solicitud_reasignacion(id_report, id_dev)
    
    return jsonify({'message': 'Solicitud de reasignacion borrada exitosamente.'}), 201

def delete_solicitud_reasignacion(id_report, id_dev):
    petition = db.solicitud_reasignacion.query.get_or_404([id_dev, id_report])
    db.session.delete(petition)
    db.session.commit()


@encargado_controller.route('/reasignacion/get/all/product/', methods=['GET'])
def get_all_reasignation_petitions_from_a_specific_product():
    id_product = request.args.get('id_product')
    if db.producto.query.filter_by(id=id_product).first() is None:
        return jsonify({'message': 'The id_product is not in the database'}), 400

    reasignation_jsons = get_reasignation_petitions_by_product_id(id_product)
    return jsonify(reasignation_jsons), 200

def get_reasignation_petitions_by_product_id(product_id):
    reports = db.reporte.query.filter_by(id_producto=product_id).all()
    reasignation_jsons = []
    for report in reports:
        petitions = db.solicitud_reasignacion.query.filter_by(id_reporte=report.id).all()
        for petition in petitions:
            petition_json = format_petition(petition)
            reasignation_jsons.append(petition_json)
    return reasignation_jsons

def format_petition(petition):
    petition_json = {
        'id_report': petition.id_reporte,
        'id_developer': petition.id_dev,
        'date': petition.fecha,
        'motivo': petition.motivo,
        'developer_name': get_developer_name(petition.id_dev),
        'report_title': get_report_title(petition.id_reporte),
        'id_prioridad': get_report_priority(petition.id_reporte)
    }
    return petition_json

def get_developer_name(dev_id):
    developer = db.desarrollador.query.filter_by(id=dev_id).first()
    return developer.nombre

def get_report_title(report_id):
    report = db.reporte.query.filter_by(id=report_id).first()
    return report.titulo

def get_report_priority(report_id):
    report = db.reporte.query.filter_by(id=report_id).first()
    return report.id_prioridad

@encargado_controller.route('/reasignacion/get/motivo/report/', methods=['GET'])
def get_motivo_reasignation_petition_from_a_specific_report():
    id_report = request.args.get('id_report')
  
    if not check_report_exists(id_report):
        return jsonify({'message': 'The id_report is not in the database'}), 400
    if not check_report_in_solicitud_reasignacion(id_report):
        return jsonify({'message': 'The id_report is not in the solicitud_reasignacion table'}), 400
    motivo = get_motivo_reasignation_petition(id_report)
    if motivo is None:
        return jsonify({'message': 'No reasignation petition found for the id_report'}), 400
    return jsonify({'motivo': motivo}), 200

def get_motivo_reasignation_petition(report_id):
    petitions = db.solicitud_reasignacion.query.filter_by(id_reporte=report_id).all()
    if not petitions:
        return None
    return petitions[0].motivo

def check_report_exists(report_id):
    return db.reporte.query.filter_by(id=report_id).first() is not None

def check_report_in_solicitud_reasignacion(report_id):
    return db.solicitud_reasignacion.query.filter_by(id_reporte=report_id).first() is not None

