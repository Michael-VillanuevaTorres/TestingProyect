import os
from flask import Flask, abort, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

from .database import db
from .controllers.report_controller import report_controller
from .controllers.user_controller import user_controller
from .controllers.product_controller import product_controller
from .controllers.encargado_controller import encargado_controller

def create_app(config):
    basedir = os.path.abspath(os.path.dirname(__file__))
    basedir = basedir[:-3]
    
    app = Flask(__name__, template_folder=basedir + '/templates')

    load_dotenv()
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('SQLALCHEMY_DATABASE_URI')

    db.init_app(app)
    Migrate(app, db)

    app.register_blueprint(report_controller)
    app.register_blueprint(user_controller)
    app.register_blueprint(product_controller)
    app.register_blueprint(encargado_controller)
    CORS(app)

    with app.app_context():
        db.session.commit()

    @app.route('/')
    @app.route('/index')
    def index():
        cliente = db.cliente.query.all()
        return cliente[0].nombre

    @app.route('/reporte/<int:id>')
    def reporte(id):
        try:
            title_reporte = db.reporte.query.filter_by(id=id).first().titulo
            description_reporte = db.reporte.query.filter_by(id=id).first().descripcion
            return render_template('reporte.html', title_reporte=title_reporte, description_reporte=description_reporte)
        except:
            abort(404)

    @app.route('/producto/<int:id>')
    def producto(id):
        try:
            title_producto = db.producto.query.filter_by(id=id).first().nombre
            if db.desarrollador.query.filter_by(id=id).first() is None:
                developer_name = "No hay desarrollador asignado"
                return render_template('producto.html', title_producto=title_producto, developer_name=developer_name)
            developer_name = "Falta implementar"
            return render_template('producto.html', title_producto=title_producto, developer_name=developer_name)
        except:
            abort(404)

    return app
