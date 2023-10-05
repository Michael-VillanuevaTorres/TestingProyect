from flask_sqlalchemy import SQLAlchemy
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os
import sys

DB_NAME = 'database.db'

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
basedir = basedir[:-3]

app = Flask(__name__, template_folder=basedir + '/templates')

app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db = SQLAlchemy(app)

class Cliente(db.Model):
    __tablename__ = 'cliente'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column('nombre', db.String(45))
    email = db.Column('email', db.String(45))
    
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email

class Comentario(db.Model):
    __tablename__ = 'comentario'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    contenido = db.Column('contenido', db.String(10000))
    id_cliente = db.Column('id_cliente', db.Integer, db.ForeignKey('cliente.id'))
    id_reporte = db.Column('id_reporte', db.Integer, db.ForeignKey('reporte.id'))
    fecha = db.Column('fecha', db.DateTime, default=db.func.current_timestamp())
    
    def __init__(self, contenido, id_reporte):
        self.contenido = contenido
        self.id_reporte = id_reporte

class Desarrollador(db.Model):
    __tablename__ = 'desarrollador'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column('nombre', db.String(45))
    email = db.Column('email', db.String(45))
    id_rol = db.Column('id_rol', db.Integer, db.ForeignKey('rol.id'))
    
    def __init__(self, nombre, email, id_rol):
        self.nombre = nombre
        self.email = email
        self.id_rol = id_rol

class Estado(db.Model):
    __tablename__ = 'estado'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column('nombre', db.String(45))
    
    def __init__(self, nombre):
        self.nombre = nombre

class Prioridad(db.Model):
    __tablename__ = 'prioridad'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column('nombre', db.String(45))
    
    def __init__(self, nombre):
        self.nombre = nombre

class Producto(db.Model):
    __tablename__ = 'producto'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column('nombre', db.String(45))
    id_encargado = db.Column('id_encargado', db.Integer, db.ForeignKey('desarrollador.id'))
    
    def __init__(self, nombre):
        self.nombre = nombre

class Reporte(db.Model):
    __tablename__ = 'reporte'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column('titulo', db.String(45))
    descripcion = db.Column('descripcion', db.String(10000))
    id_developer = db.Column('id_developer', db.Integer, db.ForeignKey('desarrollador.id'))
    id_estado = db.Column('id_estado', db.Integer, db.ForeignKey('estado.id'), default=0)
    id_prioridad = db.Column('id_prioridad', db.Integer, db.ForeignKey('prioridad.id'), default=0)
    likes = db.Column('likes', db.Integer, default=0)
    id_producto = db.Column('id_producto', db.Integer, db.ForeignKey('producto.id'))
    fecha = db.Column('fecha', db.DateTime, default=db.func.current_timestamp())
    id_cliente = db.Column('id_cliente', db.Integer, db.ForeignKey('desarrollador.id'))
    
    def __init__(self, titulo, descripcion, id_producto, id_cliente):
        self.titulo = titulo
        self.descripcion = descripcion
        self.id_producto = id_producto
        self.id_cliente = id_cliente
    
    def add_estado(self, id_estado):
        self.id_estado = id_estado
    
    def add_prioridad(self, id_prioridad):
        self.id_prioridad = id_prioridad
    
    def add_developer(self, id_developer):
        self.id_developer = id_developer
    
    def add_likes(self, like):
        self.likes = self.likes + like

class Rol(db.Model):
    __tablename__ = 'rol'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column('nombre_rol', db.String(45))
    
    def __init__(self, nombre):
        self.nombre = nombre

class ClienteProducto(db.Model):
    __tablename__ = 'cliente_producto'
    id_cliente = db.Column('id_cliente', db.Integer, db.ForeignKey('cliente.id'), primary_key=True)
    id_producto = db.Column('id_producto', db.Integer, db.ForeignKey('producto.id'), primary_key=True)
    
    def __init__(self, id_cliente, id_producto):
        self.id_cliente = id_cliente
        self.id_producto = id_producto

class DesarrolladorProducto(db.Model):
    __tablename__ = 'desarrollador_producto'
    id_desarrollador = db.Column('id_desarrollador', db.Integer, db.ForeignKey('desarrollador.id'), primary_key=True)
    id_producto = db.Column('id_producto', db.Integer, db.ForeignKey('producto.id'), primary_key=True)
    
    def __init__(self, id_desarrollador, id_producto):
        self.id_desarrollador = id_desarrollador
        self.id_producto = id_producto

class SolicitudReasignacion(db.Model):
    __tablename__ = 'solicitud_reasignacion'
    id_dev = db.Column('id_dev', db.Integer, db.ForeignKey('desarrollador.id'), primary_key=True)
    id_reporte = db.Column('id_reporte', db.Integer, db.ForeignKey('reporte.id'), primary_key=True)
    motivo = db.Column('motivo', db.String(10000))
    fecha = db.Column('fecha', db.DateTime, default=db.func.current_timestamp())
    
    def __init__(self, id_report, id_developer, motivo):
        self.id_reporte = id_report
        self.id_dev = id_developer
        self.motivo = motivo

class Like(db.Model):
    __tablename__ = 'like'
    id_desarrollador = db.Column('id_desarrollador', db.Integer, db.ForeignKey('desarrollador.id'), primary_key=True)
    id_reporte = db.Column('id_reporte', db.Integer, db.ForeignKey('reporte.id'), primary_key=True)
    
    def __init__(self, id_desarrollador, id_reporte):
        self.id_desarrollador = id_desarrollador
        self.id_reporte = id_reporte


with app.app_context():
    db.create_all()