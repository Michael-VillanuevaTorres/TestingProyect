
import sys
import os
from flask import Flask, abort, render_template, make_response
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '/website/database')))
from flask_cors import CORS
from website.database import db,app
from flask import jsonify

from website.database import Cliente, Comentario, Desarrollador, Estado, Prioridad, Producto, Reporte, Rol, ClienteProducto, DesarrolladorProducto, SolicitudReasignacion, Like 

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

@app.route('/products/all', methods=['GET'])
def get_all_products():
    products = db.producto.query.all()
    products_json = []
    for product in products:
        product_json = {}
        product_json['id'] = product.id
        product_json['nombre'] = product.nombre
        product_json['id_encargado'] = product.id_encargado
        products_json.append(product_json)
    return jsonify(products_json), 200

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


if '__name__' == '__main__':
    
    with app.app_context():
        app.db.create_all()

    from .website.controllers.report_controller import report_controller
    from .website.controllers.user_controller import user_controller
    from .website.controllers.product_controller import product_controller
    from .website.controllers.old_encargado_controller import encargado_controller

    app.register_blueprint(report_controller)
    app.register_blueprint(user_controller)
    app.register_blueprint(product_controller)
    app.register_blueprint(encargado_controller)
    CORS(app, supports_credentials=True)
    app.config['CORS_HEADERS'] = 'Content-Type'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['SESSION_COOKIE_SECURE'] = True
    app.config['SESSION_COOKIE_SAMESITE'] = 'None'
    CORS(app,origins='localhost:3000')

    app.run(app.run(debug = True))


