from app.product import bp as app

@app.route('/pending_reports', methods=['GET'])
def get_pending_reports():
    pass

@app.route('/get', methods=['GET'])
def get_product():
    pass 

@app.route('/reports/all', methods=['GET'])
def get_all_reports_from_product():
    pass  

@app.route('/get/all', methods=['GET'])
def get_all_products():
    pass

@app.route('/developers/all', methods=['GET'])
def get_developers_from_product():
    pass