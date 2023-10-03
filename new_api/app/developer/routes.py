from app.user import bp as app

@app.route('/reports/', methods=['GET'])
def get_reportes_from_dev():
    pass

@app.route('/all/report-product/', methods=['GET'])
def get_all_reports_and_products():
    pass

@app.route('/all-reportes-related-to-products/', methods=['GET'])
def get_all_reports_related_to_products():
    pass

@app.route('/info/', methods=['GET'])
def get_dev_info():
    pass    

async def add_cliente(nombre, email):
    pass

async def add_id_rol(nombre):
    pass