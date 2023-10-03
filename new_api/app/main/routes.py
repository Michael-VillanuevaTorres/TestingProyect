from app.main import bp as app

@app.route('/')
def index():
   pass

@app.route('/reporte/<int:id>')
def reporte(id):
    pass

@app.route('/producto/<int:id>')
def producto(id):
    pass