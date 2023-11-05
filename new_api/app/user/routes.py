from app.user import bp as app
from app.extensions import db

from app.utils import report_to_list

from flask import jsonify, request

from app.models.report import Report
from app.models.developer import Developer
from app.models.like import Like

@app.route('/likes', methods=['GET'])
def get_likes_from_user():
    id_user = request.args.get('id_user')
    developer = Developer.query.filter_by(id=id_user).first()
    if developer is None:
        return jsonify({'message': 'el usuariao no existe'})
    #get all the where in the table reporte the id_dev is the same as the id_dev in the request
    likes = Like.query.filter_by(id_developer=id_user).all()
    reports = []
    for like in likes:
        id_report = like.id_report
        report = Report.query.get_or_404(id_report)
        reports.append(report)
    reports = [report_to_list(report) for report in reports]
    #return the json
    return jsonify(reports)

@app.route('/reports', methods=['GET'])
def get_reports_from_user():
    id_user = request.args.get('id_user')
    user = Report.query.filer_by(id=id_user).first()
    
    if user is None:
        return jsonify({'message': 'el user no existe'}), 400
    
    reports = Report.query.filter_by(id=id_user).all()
    reports_json = [report_to_list(report) for report in reports]
    return jsonify(reports_json), 200
