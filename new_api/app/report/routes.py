from app.report import bp as app

@app.route('/get/comments', methods=['GET'])
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

@app.route('/get', methods=['GET'])
def get_report():
    pass

@app.route('/get/all', methods=['GET'])
def get_all_reports():
    pass

@app.route('/all/product/', methods=['GET'])
def get_all_reports_from_a_specific_product():
    pass

@app.route('/get', methods=['GET'])
def get_single_report():
    pass

@app.route('/update/estado', methods=['POST'])
def update_estado():
    pass

@app.route('/update/prioridad', methods=['POST'])
def update_prioridad():
    pass

@app.route('/check/estados', methods=['GET'])
def check_estados():
    pass

def commit_comment(description, id_report):
    pass

def commit_like(id_user, id_reporte):
    pass

def commit_report(titulo,descripcion,id_producto,id_cliente):
    pass

def object_to_list_comment(comment):
    pass

def object_to_list_report(report):
    pass

def object_to_list_estado(estado):
    pass

@app.route('/estados/all', methods=['GET'])
def all_estados():
    pass

@app.route('/add/developer/', methods=['POST'])
def add_developer():
    pass

def commit_developer(report, id_developer):
    pass

@app.route('/prioridad/all', methods=['GET'])
def all_prioridad():
    pass

def object_to_list_prioridad(prioridad):
    pass

def add_desarrollador_producto(id_desarrollador, id_producto):
    pass

def add_estado(nombre):
    pass

def add_producto(nombre):
    pass