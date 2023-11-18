from app.reassignment import bp as app
from app.extensions import db
from app.models.report import Report
from app.models.developer import Developer
from app.models.reassignment import Reassignment
from app.models.product import Product

from flask import jsonify, request


@app.route('/add', methods=['POST'])
def add_reassignment_petition():
    data=request.json
    id_report = request.args.get('id_report')
    id_developer = request.args.get('id_developer')
    
    db.get_or_404(Report, id_report)
    db.get_or_404(Developer, id_developer)
    
    if db.session.scalar(db.select(Reassignment).where(Reassignment.id_developer==id_developer, Reassignment.id_report==id_report)) is None:
        commit_reassignment(id_report,id_developer, data['motivo'])
        return jsonify({'message': 'solicitud de reasignacion agregada exitosamente.'}), 201    
    
    return jsonify({'message': 'The id_report is already in the database'}), 400
    
    
@app.route('/get', methods=['GET'])
def get_reassignment():
    id_report = request.args.get('id_report')
    reassignment = db.session.scalar(db.select(Reassignment).where(Reassignment.id_report==id_report))
    
    return jsonify(reassignment.serialize()), 200
    

@app.route('/delete', methods=['DELETE'])
def delete_reassignment_petition():

    pass

@app.route('/product/all', methods=['GET'])
def get_all_reassignment_petitions_from_product():
    id_product = request.args.get('id_product')
    
    db.get_or_404(Product, id_product)
    
    reassignments = db.session.query(Reassignment).join(Report).filter(Report.id_product == id_product).all()
    
    return jsonify([reassignment.serialize() for reassignment in reassignments]), 200
    

@app.route('/reason', methods=['GET'])
def get_reassignment_reason():
    pass

def commit_reassignment(id_report,id_developer, motivo):
    reassignment = Reassignment(id_report,id_developer,motivo)
    db.session.add(reassignment)
    db.session.commit()
