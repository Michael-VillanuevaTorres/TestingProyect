from app.product import bp as app

@app.route('/get/reports', methods=['GET'])
def get_reports():
    pass

@app.route('/get', methods=['GET'])
def get_product():
    pass 

@app.route('/get/all_reports', methods=['GET'])
def get_all_reports_from_product():
    pass  

@app.route('/all', methods=['GET'])
def get_all_products():
    pass

@app.route('/get/developers', methods=['GET'])
def get_product_from_developer():
    pass