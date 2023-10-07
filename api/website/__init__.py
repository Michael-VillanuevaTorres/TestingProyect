import os
from flask import Flask, abort, render_template
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from faker import Faker
import random

desarrolladores_fake = [
    "Desarrollador 1",
    "Desarrollador 2",
]
desarrolladores_fake2 = [
    "Desarrollador 3",
    "Desarrollador 4",
]

# Generar clientes
clientes_fake = [
    "Cliente 1",
    "Cliente 2",
    "Cliente 3",
]

# Generar productos
productos_fake = [
    "Producto 1",
    "Producto 2",
    "Producto 3",
    "Producto 4",
]
emailcliente_fake = [
    "email1@example.com",
    "email2@example.com", 
    "email3@example.com"
]
emaildesarrollador_fake =[
    "desarrollador1@example.com"
    "desarrollador2@example.com",
]
emaildesarrollador_fake2 =[
    "desarrollador3@example.com",
    "desarrollador4@example.com"
]

db = SQLAlchemy()


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

    @app.route('/ver_datos')
    def ver_datos():
        productos = Producto.query.all()
        reportes = Reporte.query.all()
        clientes = Cliente.query.all()
        desarolladores = Desarrollador.query.all()

        data = [{'nombre': producto.nombre,'id':producto.id, 'enc': producto. id_encargado} for producto in productos]
        data2 = [{'nombreR': reporte.titulo,'idR':reporte.id, 'idDeveloper':reporte.id_developer} for reporte in reportes]
        data3 = [{'nombreC': cliente.nombre,'idC':cliente.id} for cliente in clientes]
        data4 = [{'nombreP': desarollador.nombre,'idP':desarollador.id} for desarollador in desarolladores]
                
        return (data+data2+data3+data4)
    

    # Ruta para eliminar los datos generados por Fake
    @app.route('/reset_fake_data') 
    def reset_fake_data():
        # Eliminar todos los objetos generados por Fake de la base de datos
        db.session.query(Desarrollador).delete()
        db.session.query(Cliente).delete()
        db.session.query(Producto).delete()
        db.session.query(Reporte).delete()

        # Cometer los cambios en la base de datos
        db.session.commit()

        return ({'message': 'Datos generados por Fake eliminados correctamente'}), 200


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
        


    @app.route('/generate_fake_data')
    def generate_fake_data():
      # Crear roles (0 y 1)

        # Crear desarrolladores (3 en total, 2 con rol 0 y 1 con rol 1)
        desarrolladores = []
        for i in range(2):
            desarrollador = Desarrollador(
                nombre=desarrolladores_fake[i-1],
                email=emaildesarrollador_fake[i-1],
                id_rol=0
            )
            desarrolladores.append(desarrollador)

        for i in range(2):
            desarrollador2 = Desarrollador(
                nombre=desarrolladores_fake2[i],
                email=emaildesarrollador_fake2[i],
                id_rol=1
            )
            desarrolladores.append(desarrollador2)

        # Crear clientes (2 en total)
        clientes = []
        for i in range(3):
            cliente = Cliente(
                nombre=clientes_fake[i],
                email=emailcliente_fake[i]
            )
            clientes.append(cliente)

        # Crear productos (4 en total)
        productos = []
        for i in range(4):
            producto = Producto(
                nombre=productos_fake[i],
            )
            productos.append(producto)
        


        db.session.add_all(desarrolladores + clientes + productos)
       
        # Crear reportes (2 por cada producto)
        for producto in productos:
            for _ in range(2):
                reporte = Reporte(
                    titulo=f"Reporte de {producto.nombre}",
                    descripcion=f"Descripción del reporte de {producto.nombre}",
                    id_producto=producto.id,
                    id_cliente=1, 
                )
                db.session.add(reporte)
                Reporte.add_developer(reporte, 1)
                

        # Agregar todos los objetos a la sesión y guardar en la base de datos
        db.session.commit()
        return "Funcionó correctamente"
        
    
    return app

def create_database(app):
    with app.app_context():
        db.create_all()
        print('Created Database!')
