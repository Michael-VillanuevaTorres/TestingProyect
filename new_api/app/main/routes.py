from app.main import bp as app

@app.route('/')
def index():
<<<<<<< HEAD
    pass
=======
   pass
>>>>>>> parent of 47d285ae (test(reports): Create tests for report paths and fix associated bugs)

@app.route('/report/<int:id>')
def reporte(id):
    pass

@app.route('/product/<int:id>')
def producto(id):
    pass