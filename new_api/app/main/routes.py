from app.main import bp as app

@app.route('/')
def index():
   return"HELLO"

@app.route('/report/<int:id>')
def reporte(id):
    pass

@app.route('/product/<int:id>')
def producto(id):
    pass