from app.report import bp as app
from app.extensions import db
from app.utils import *
from flask import jsonify, request


@app.route('/add/comment', methods=['POST'])
def add_comment_to_report():
    data = request.json
    id_report = request.args.get('id_report')
    if db.report.query.filter_by(id=id_report).first() is None:
        return jsonify({'message': 'The id_report is not in the database'}), 400
    
    if data.get('text') is None:
        return jsonify({'message': 'Comment not added. Text is needed'}), 400
    
    commit_comment(data['text'], id_report)
    
    return jsonify({'message': 'Comment added successfully.'}), 201

@app.route('/add/like', methods=['POST'])
def add_like_to_report():
    id_report = request.args.get('id_report')
    id_user = request.args.get('id_user')
    
    report = db.report.query.get_or_404(id_report)
    
    if db.like.query.filter_by(id_developer=id_user, id_report=id_report).first() is not None:
        return jsonify({'message': 'The like is already in the database'}), 400
    
    commit_like(id_user, id_report)
    report.add_likes(1)

    return jsonify({'message': 'like added successfully.'}), 201


@app.route('/add', methods=['POST'])
def add_report():
    data = request.json
    id_product = request.args.get('id_product')
    id_user = request.args.get('id_user')
    
    if db.product.query.filter_by(id=id_product).first() is None:
        return jsonify({'message': 'The id_product is not in the database'}), 400
    
    if data.get('title') is None:
        return jsonify({'message': 'Report not added. Title is needed'}), 400
    
    if data.get('description') is None:
        return jsonify({'message': 'Report not added. Description is needed'}), 400
    
    commit_report(data['title'], data['description'], id_product, id_user)
    
    return jsonify({'message': 'Report added successfully.'}), 201

@app.route('/comments', methods=['GET'])
def get_comments_form_report():
    id_report = request.args.get('id_report')

    if db.report.query.filter_by(id=id_report).first() is None:
        return jsonify({'message': 'The id_report is not in the database'}), 400

    comments = db.comment.query.filter_by(id_report=id_report).all()
    comments_json = [comment_to_list(comment) for comment in comments]

    return jsonify(comments_json), 200

@app.route('/get/more', methods=['GET'])
def get_number_of_reports():
    quantity = request.args.get('quantity')
    id_product = request.args.get('id_product')

    if db.product.query.filter_by(id=id_product).first() is None:
        return jsonify({'message': 'The id_product is not in the database'}), 400

    if quantity is None:
        return jsonify({'message': 'Quantity not specified'}), 400

    if int(quantity) > db.report.query.filter_by(id_product=id_product).count():
        return jsonify({
            'message': f'The quantity is bigger than the number of reports. Quantity asked is: {quantity} The number of reports with the product id is: {db.report.query.filter_by(id_product=id_product).count()}'
        }), 400

    reports = db.report.query.filter_by(id_product=id_product).order_by(db.report.likes.desc()).limit(quantity).all()
    reports_json = [report_to_list(report) for report in reports]

    return jsonify(reports_json), 200

@app.route('/get/all', methods=['GET'])
def get_all_reports():
    reports = db.reporte.query.all()
    reports_json = [report_to_list(report) for report in reports]

    return jsonify(reports_json), 200

@app.route('/product/all', methods=['GET'])
def get_all_reports_from_product():
    id_product = request.args.get('id_product')
    if db.product.query.filter_by(id=id_product).first() == None:
        return jsonify({'message': 'The id_product is not in the database'}), 400
    reports = db.report.query.filter_by(id_product=id_product).all()
    #revisar si se quiere asi o que solamente entregue una lista vacia
    if len(reports) == 0:
        return jsonify({'message': 'There are no reports with that id_product'}), 400
    
    reports_json = [report_to_list(report) for report in reports]
    
    return jsonify(reports_json), 200

@app.route('/get', methods=['GET'])
def get_report():
    id_report = request.args.get('id_report')
    report = db.report.query.get_or_404(id_report)
    
    report_json = [report_to_list(report) for report in report]
    
    return jsonify(report_json), 200

@app.route('/update/state', methods=['POST'])
def update_state_of_report():
    id_report = request.args.get('id_report')
    id_state = request.args.get('id_state')
    
    if db.report.query.filter_by(id=id_report).first() == None:
        return jsonify({'message': 'The id_report is not in the database'}), 400
    if db.state.query.filter_by(id=id_state).first() == None:
        return jsonify({'message': 'The id_state is not in the database'}), 400
    
    report = db.report.query.get_or_404(id_report)
    report.id_state = id_state
    db.session.commit()
    
    return jsonify({'message': 'state updated successfully.'}), 201
    

@app.route('/update/priority', methods=['POST'])
def update_priority_of_report():
    id_report = request.args.get('id_report')
    id_priority = request.args.get('id_priority')
    
    if db.report.query.filter_by(id=id_report).first() == None:
        return jsonify({'message': 'The id_report is not in the database'}), 400
    if db.priority.query.filter_by(id=id_priority).first() == None:
        return jsonify({'message': 'The id_state is not in the database'}), 400
    
    report = db.report.query.get_or_404(id_report)
    report.id_priority = id_priority
    db.session.commit()
    
    return jsonify({'message': 'state updated successfully.'}), 201

@app.route('/state', methods=['GET'])
def check_possibles_states_to_report():
    id_report= request.args.get('id_report')
    
    if db.report.query.filter_by(id=id_report).first() == None:
        return jsonify({'message': 'The id_report is not in the database'}), 400
    #return all the states, but the id=0 and the current id_state
    states = db.state.query.filter(db.state.id != 0).filter(db.state.id != db.report.query.get_or_404(id_report).id_state).all()
    states_json = []
    for state in states:
        states_json.append(state_to_list(state))

@app.route('/state/all', methods=['GET'])
def all_states():
    #return all the states
    states = db.state.query.all()
    states_json = []
    
    for state in states:
        states_json.append(state_to_list(state))
        
    return jsonify(states_json), 200

@app.route('/add/developer/', methods=['POST'])
def add_developer():
    id_report = request.args.get('id_report')
    id_developer = request.args.get('id_dev')
    
    if db.report.query.filter_by(id=id_report).first() is None:
        return jsonify({'message': 'The id_report is not in the database'}), 400
    if db.developer.query.filter_by(id=id_developer).first() is None:
        return jsonify({'message': 'The id_developer is not in the database'}), 400
    
    report = db.report.query.get_or_404(id_report)
    commit_developer(report, id_developer)
    
    return jsonify({'message': 'Developer added successfully.'}), 201


@app.route('/priority/all', methods=['GET'])
def all_prioritys():
    prioritys = db.priority.query.all()
    prioritys_json = [priority_to_list(priority) for priority in prioritys]
        
    return jsonify(prioritys_json), 200

def commit_developer(report, id_developer):
    report.id_developer = id_developer
    report.id_state = 1
    db.session.commit()

def commit_comment(description, id_report):
    comment = db.comment(description, id_report)
    db.session.add(comment)
    db.session.commit()

def commit_like(id_user, id_report):
    like = db.like(id_user,id_report)
    db.session.add(like)
    db.session.commit()

def commit_report(title,description,id_product,id_user):
    report = db.report(title, description, id_product,id_user)
    db.session.add(report)
    db.session.commit()
    
def add_state(name):
    state = db.state(name)
    db.session.add(state)
    db.session.commit()
