from app.report import bp as app
from app.extensions import db

from flask import jsonify, request

@app.route('/comments', methods=['GET'])
def get_comments_form_report():
    pass

@app.route('/add/comment', methods=['POST'])
def add_comment_to_report():
    pass

@app.route('/add/like', methods=['POST'])
def add_like_to_comment():
    pass

@app.route('/add', methods=['POST'])
def add_report():
    pass

@app.route('/get/more', methods=['GET'])
def get_number_of_reports():
    pass

@app.route('/get/all', methods=['GET'])
def get_all_reports():
    pass

@app.route('/product/all', methods=['GET'])
def get_all_reports_from_product():
    pass

@app.route('/get', methods=['GET'])
def get_report():
    pass

@app.route('/update/state', methods=['POST'])
def update_state_of_report():
    pass

@app.route('/update/priority', methods=['POST'])
def update_priority_of_report():
    pass

@app.route('/state', methods=['GET'])
def check_possibles_states_to_report():
    pass

@app.route('/state/all', methods=['GET'])
def all_states():
    pass

@app.route('/add/developer/', methods=['POST'])
def add_developer():
    pass

@app.route('/priority/all', methods=['GET'])
def all_prioritys():
    pass

def commit_developer(report, id_developer):
    pass

def commit_comment(description, id_report):
    pass

def commit_like(id_user, id_reporte):
    pass

def commit_report(titulo,descripcion,id_producto,id_cliente):
    pass

def add_desarrollador_producto(id_desarrollador, id_producto):
    pass

def add_estado(nombre):
    pass
