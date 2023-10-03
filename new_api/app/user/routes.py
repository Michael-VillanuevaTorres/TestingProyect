from app.user import bp as app

@app.route('/liked/', methods=['GET'])
def get_likes_from_user():
    pass

@app.route('/reports/', methods=['GET'])
def get_user_reports():
    pass  

async def add_cliente(nombre, email):
    pass

async def add_id_rol(nombre):
    pass