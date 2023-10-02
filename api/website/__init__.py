import os
from flask import Flask, abort, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from faker import Faker

db = SQLAlchemy()
DB_NAME = 'database.db'
fake = Faker()

def create_app():
    basedir = os.path.abspath(os.path.dirname(__file__))
    basedir = basedir[:-3]
    
    app = Flask(__name__, template_folder=basedir + '/templates')

    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    #Migrate(app, db)
    
    from .controllers.report_controller import report_controller
    from .controllers.user_controller import user_controller
    from .controllers.product_controller import product_controller
    from .controllers.old_encargado_controller import encargado_controller

    app.register_blueprint(report_controller)
    app.register_blueprint(user_controller)
    app.register_blueprint(product_controller)
    app.register_blueprint(encargado_controller)
    CORS(app)


    from .database import Cliente, Comentario, Desarrollador, Estado, Prioridad, Producto, Reporte, Rol, ClienteProducto, DesarrolladorProducto, SolicitudReasignacion, Like 
    
    create_database(app)

    @app.route('/')
    @app.route('/index')
    def index():
        clientes = Cliente.query.all()
        if clientes:
            return clientes[0].nombre
        else:
            return "No hay clientes en la base de datos"

    @app.route('/reporte/<int:id>')
    def reporte(id):
        try:
            title_reporte = Reporte.query.filter_by(id=id).first().titulo
            description_reporte = Reporte.query.filter_by(id=id).first().descripcion
            return render_template('reporte.html', title_reporte=title_reporte, description_reporte=description_reporte)
        except:
            abort(404)
    @app.route('/ver_datos/productos')
    def ver_productos():
        productos = Producto.query.all()
        data = [{'nombre': producto.nombre} for producto in productos]
        return (data)

    @app.route('/producto/<int:id>')
    def producto(id):
        try:
            title_producto = Producto.query.filter_by(id=id).first().nombre
            if Desarrollador.query.filter_by(id=id).first() is None:
                developer_name = "No hay desarrollador asignado"
                return render_template('producto.html', title_producto=title_producto, developer_name=developer_name)
            developer_name = "Falta implementar"
            return render_template('producto.html', title_producto=title_producto, developer_name=developer_name)
        except:
            abort(404)


    @app.route('/generate_fake_data')
    def generate_fake_data():
        from faker import Faker  # Asegúrate de importar Faker
        fake = Faker()  # Crea una instancia de Faker

        # Crear roles (0 y 1)

        # Crear desarrolladores (3 en total, 2 con rol 0 y 1 con rol 1)
        desarrolladores = []
        for _ in range(2):
            desarrollador = Desarrollador(
                nombre=fake.name(),
                email=fake.email(),
                id_rol=0
            )
            desarrolladores.append(desarrollador)

        for _ in range(1):
            desarrollador = Desarrollador(
                nombre=fake.name(),
                email=fake.email(),
                id_rol=1
            )
            desarrolladores.append(desarrollador)

        # Crear clientes (2 en total)
        clientes = []
        for _ in range(2):
            cliente = Cliente(
                nombre=fake.company(),
                email=fake.email()
            )
            clientes.append(cliente)

        # Crear productos (4 en total)
        productos = []
        for _ in range(4):
            producto = Producto(
                nombre=fake.word(),
            )
            productos.append(producto)

        db.session.add_all(desarrolladores + clientes + productos)

        # Crear reportes (2 por cada producto)
        for producto in productos:
            for _ in range(2):
                reporte = Reporte(
                    titulo=fake.sentence(),
                    descripcion=fake.paragraph(),
                    id_producto=producto.id,
                    id_cliente=clientes[fake.random_int(0, 1)].id,  # Escoge un cliente aleatorio
                )
                db.session.add(reporte)

        # Agregar todos los objetos a la sesión y guardar en la base de datos
        db.session.commit()
        return "Funcionó correctamente"
        
    return app

def create_database(app):
    with app.app_context():
        db.create_all()
        print('Created Database!')
