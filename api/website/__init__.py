import os
from flask import Flask, abort, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()
DB_NAME = 'database.db'

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
    from .controllers.encargado_controller import encargado_controller

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

    return app

def create_database(app):
    with app.app_context():
        db.create_all()
        print('Created Database!')
