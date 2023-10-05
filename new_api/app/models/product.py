from app.extensions import db

class Product(db.Model):
    __tablename__ = 'product'
    
    id           = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name         = db.Column('name', db.String(45))
    id_developer = db.Column('id_developer', db.Integer, db.ForeignKey('developer.id'))
    
    def __init__(self, name):
        self.nombre = name
