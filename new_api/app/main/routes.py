from app.main import bp as app

@app.route('/')
def index():
<<<<<<< HEAD
   return"HELLO"
=======
    return 'Hello World'
>>>>>>> main

@app.route('/report/<int:id>')
def reporte(id):
    pass

@app.route('/product/<int:id>')
def producto(id):
    pass