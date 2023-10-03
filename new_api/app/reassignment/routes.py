from app.reassignment import bp as app


@app.route('/add', methods=['POST'])
def add_reassignment_petition():
    pass

@app.route('/delete', methods=['DELETE'])
def delete_reassignment_petition():
    pass

@app.route('/product/all', methods=['GET'])
def get_all_reassignment_petitions_from_product():
    pass

@app.route('/reason', methods=['GET'])
def get_reassignment_reason():
    pass
