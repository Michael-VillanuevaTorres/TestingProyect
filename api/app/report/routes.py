from app.report import bp as app
from app.extensions import db
from app.utils import *
from flask import jsonify, request

from app.models.comment import Comment
from app.models.developer import Developer
from app.models.like import Like
from app.models.priority import Priority
from app.models.product import Product
from app.models.report import Report
from app.models.state import State
from app.models.reassignment import Reassignment
from app.models.relationship_developer_product import RelationshipDeveloperProduct
from app.models.relationship_user_product import RelationshipUserProduct 
from app.models.report import Report
from app.models.role import Role
from app.models.user import User

from app.product.routes import add_developer_product

desarrolladores_fake = [
    "Desarrollador 1",
    "Desarrollador 2",
]
desarrolladores_fake2 = [
    "Desarrollador 3",
    "Desarrollador 4",
]

# Generar clientes
clientes_fake = [
    "Cliente 1",
    "Cliente 2",
    "Cliente 3",
]

# Generar productos
productos_fake = [
    "Producto 1",
    "Producto 2",
    "Producto 3",
    "Producto 4",
]
emailcliente_fake = [
    "email1@example.com",
    "email2@example.com", 
    "email3@example.com"
]
emaildesarrollador_fake =[
    "desarrollador1@example.com"
    "desarrollador2@example.com",
]
emaildesarrollador_fake2 =[
    "desarrollador3@example.com",
    "desarrollador4@example.com"
]


@app.route('/add/comment', methods=['POST'])
def add_comment_to_report():
    data = request.json
    id_report = request.args.get('id_report')
    if Report.query.filter_by(id=id_report).first() is None:
        return jsonify({'message': 'The id_report is not in the database'}), 400
    
    if data.get('text') is None:
        return jsonify({'message': 'Comment not added. Text is needed'}), 400
    
    commit_comment(data['text'], id_report)
    
    return jsonify({'message': 'Comment added successfully.'}), 201

@app.route('/add/like', methods=['POST'])
def add_like_to_report():
    id_report = request.args.get('id_report')
    id_user = request.args.get('id_user')
    
    report = Report.query.get_or_404(id_report)

    if Like.query.filter_by(id_developer=id_user, id_report=id_report).first() is not None:
        return jsonify({'message': 'The like is already in the database'}), 400
    
    commit_like(report,id_user, id_report)

    return jsonify({'message': 'like added successfully.'}), 201


@app.route('/add', methods=['POST'])
def add_report():
    data = request.json
    id_product = request.args.get('id_product')
    id_user = request.args.get('id_user')
    
    if Product.query.filter_by(id=id_product).first() is None:
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

    if Report.query.filter_by(id=id_report).first() is None:
        return jsonify({'message': 'The id_report is not in the database'}), 400

    comments = Comment.query.filter_by(id_report=id_report).all()
    comments_json = [comment_to_list(comment) for comment in comments]

    return jsonify(comments_json), 200

@app.route('/get/more', methods=['GET'])
def get_number_of_reports():
    quantity = request.args.get('quantity')
    id_product = request.args.get('id_product')

    if Product.query.filter_by(id=id_product).first() is None:
        return jsonify({'message': 'The id_product is not in the database'}), 400

    if quantity is None:
        return jsonify({'message': 'Quantity not specified'}), 400

    if int(quantity) > Report.query.filter_by(id_product=id_product).count():
        return jsonify({
            'message': f'The quantity is bigger than the number of reports. Quantity asked is: {quantity} The number of reports with the product id is: {Report.query.filter_by(id_product=id_product).count()}'
        }), 400

    reports = Report.query.filter_by(id_product=id_product).order_by(Report.likes.desc()).limit(quantity).all()
    reports_json = [report_to_list(report) for report in reports]

    return jsonify(reports_json), 200

@app.route('/get/all', methods=['GET'])
def get_all_reports():
    reports = db.session.query(Report).all()
    
    reports_json = [report.serialize() for report in reports]

    return jsonify(reports_json), 200

@app.route('/product/all', methods=['GET'])
def get_all_reports_from_product():
    id_product = request.args.get('id_product')
    if Product.query.filter_by(id=id_product).first() == None:
        return jsonify({'message': 'The id_product is not in the database'}), 400
    reports = Report.query.filter_by(id_product=id_product).all()
    print(reports)
    
    #revisar si se quiere asi o que solamente entregue una lista vacia
    if len(reports) == 0:
        return jsonify({'message': 'There are no reports with that id_product'}), 400
    
    reports_json = [report_to_list(report) for report in reports]
    
    return jsonify(reports_json), 200

@app.route('/get', methods=['GET'])
def get_report():
    id_report = request.args.get('id_report')
    report = Report.query.get_or_404(id_report)
    
    report_json = report_to_list(report)
    
    return jsonify(report_json), 200

@app.route('/update/state', methods=['POST'])
def update_state_of_report():
    id_report = request.args.get('id_report')
    id_state = request.args.get('id_state')

    if Report.query.filter_by(id=id_report).first() == None:
        return jsonify({'message': 'The id_report is not in the database'}), 400
    if State.query.filter_by(id=id_state).first() == None:
        return jsonify({'message': 'The id_state is not in the database'}), 400
    
    report = Report.query.get_or_404(id_report)
    report.id_state = id_state
    db.session.commit()
    
    return jsonify({'message': 'state updated successfully.'}), 201
    

@app.route('/update/priority', methods=['POST'])
def update_priority_of_report():
    id_report = request.args.get('id_report')
    id_priority = request.args.get('id_priority')
    
    if Report.query.filter_by(id=id_report).first() == None:
        return jsonify({'message': 'The id_report is not in the database'}), 400
    if Priority.query.filter_by(id=id_priority).first() == None:
        return jsonify({'message': 'The id_state is not in the database'}), 400
    
    report = Report.query.get_or_404(id_report)
    report.id_priority = id_priority
    db.session.commit()
    
    return jsonify({'message': 'state updated successfully.'}), 201

@app.route('/state', methods=['GET'])
def check_possibles_states_to_report():
    id_report = request.args.get('id_report')

    if Report.query.filter_by(id=id_report).first() is None:
        return jsonify({'message': 'The id_report is not in the database'}), 400

    # return all the states, but the id=0 and the current id_state
    states = State.query.filter(State.id != 0).filter(State.id != Report.query.get_or_404(id_report).id_state).all()
    states_json = []
    for state in states:
        states_json.append(state_to_list(state))

    return jsonify(states_json), 200

@app.route('/state/all', methods=['GET'])
def all_states():
    #return all the states
    states = State.query.all()
    states_json = []
    
    for state in states:
        states_json.append(state_to_list(state))
        
    return jsonify(states_json), 200

@app.route('/add/developer/', methods=['POST'])
def add_developer():
    id_report = request.args.get('id_report')
    id_developer = request.args.get('id_dev')
    
    if Report.query.filter_by(id=id_report).first() is None:
        return jsonify({'message': 'The id_report is not in the database'}), 400
    if Developer.query.filter_by(id=id_developer).first() is None:
        return jsonify({'message': 'The id_developer is not in the database'}), 400
    
    report = Report.query.get_or_404(id_report)
    commit_developer(report, id_developer)
    
    return jsonify({'message': 'Developer added successfully.'}), 201


@app.route('/priority/all', methods=['GET'])
def all_prioritys():
    prioritys = Priority.query.all()
    prioritys_json = [priority_to_list(priority) for priority in prioritys]
        
    return jsonify(prioritys_json), 200

@app.route('/reset_fake_data', methods=['GET']) 
def reset_fake_data():
    # Eliminar todos los objetos generados por Fake de la base de datos
    db.session.query(Developer).delete()
    db.session.query(User).delete()
    db.session.query(Product).delete()
    db.session.query(Report).delete()
    db.session.query(Like).delete()
    db.session.query(Priority).delete()
    db.session.query(Reassignment).delete()
    db.session.query(RelationshipDeveloperProduct).delete()
    db.session.query(RelationshipUserProduct).delete()
    db.session.query(State).delete()
    db.session.query(Role).delete()
    db.session.query(Comment).delete()



    # Cometer los cambios en la base de datos
    db.session.commit()

    return ({'message': 'Datos generados por Fake eliminados correctamente'}), 200

@app.route('/generate_fake_data')
def generate_fake_data():

    # Roles
    developer_role = Role(name='developer')
    db.session.add(developer_role)
    
    admin_role = Role(name='admin')
    db.session.add(admin_role)

    # Commit changes
    db.session.commit()

    # Developers
    default_developer = Developer(name="default_developer", email='default@email.com', id_role=1)
    default_developer2 = Developer(name="default_developer2", email='default2@email.com', id_role=1)
    default_developer3 = Developer(name="default_developer3", email='default3@email.com', id_role=2)
    db.session.add(default_developer)
    db.session.add(default_developer2)
    db.session.add(default_developer3)

    # Commit changes
    db.session.commit()

    # Products
    default_product = Product(name='default_product')
    default_product2 = Product(name='default_product2')
    db.session.add(default_product)
    db.session.add(default_product2)

    # Commit changes
    db.session.commit()

    default_product.id_developer = 1
    default_product2.id_developer = 1  


    # Users
    default_user = User(name='default_user', email='default@email.com')
    db.session.add(default_user)

    # Commit changes
    db.session.commit()
    
    # RelationshipDeveloperProduct
    default_relationship = RelationshipDeveloperProduct(id_product=1, id_developer=1)
    db.session.add(default_relationship)
    
    # States
    default_state = State(name='Pendiente')
    default_state2 = State(name='En proceso')
    default_state3 = State(name='Cerrado')

    db.session.add(default_state)
    db.session.add(default_state2)
    db.session.add(default_state3)

    # Prioritys
    default_priority = Priority(name='Baja')
    default_priority2 = Priority(name='Media')
    default_priority3 = Priority(name='Alta')
    db.session.add(default_priority)
    db.session.add(default_priority2)
    db.session.add(default_priority3)

    # Reports
    default_report = Report(title='default_report', description='default description', id_product=1, id_user=1)
    db.session.add(default_report)

    default_report2 = Report(title='default_report2', description='default2 description', id_product=2, id_user=1)
    db.session.add(default_report2)
    # Commit changes
    db.session.commit()

    default_report.id_state = 1
    default_report2.id_state = 1  


    # Commit changes
    db.session.commit()

    return "Funcionó correctamente"

def commit_developer(report, id_developer):
    report.id_developer = id_developer
    report.id_state = 1
    db.session.commit()

def commit_comment(description, id_report):
    comment = Comment(description, id_report)
    db.session.add(comment)
    db.session.commit()

def commit_like(report,id_user, id_report):
    like = Like(id_user,id_report)
    report.add_likes(1)
    db.session.add(like)
    db.session.commit() 

def commit_report(title,description,id_product,id_user):
    report = Report(title=title, description=description, id_product=id_product, id_user=id_user)
    db.session.add(report)
    db.session.commit()
    

def add_state(name):
    state = State(name)
    db.session.add(state)
    db.session.commit()

