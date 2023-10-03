from app.reassignment import bp as app


@app.route('/add/', methods=['POST'])
def add_reasingation_petition():
    pass

@app.route('/delete/', methods=['DELETE'])
def delete_reasingation_petition():
    pass

@app.route('/get/all/product/', methods=['GET'])
def get_all_reasignation_petitions_from_a_specific_product():
    pass

@app.route('/get/motivo/report/', methods=['GET'])
def get_motivo_reasignation_petition_from_a_specific_report():
    pass

def add_solicitud_reasignacion(id_report,id_developer, motivo):
    pass