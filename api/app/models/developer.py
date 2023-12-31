from app.extensions import db

class Developer(db.Model):
    __tablename__ = 'developer'
    
    id      = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name    = db.Column('name', db.String(45))
    email   = db.Column('email', db.String(45))
    id_role = db.Column('id_role', db.Integer, db.ForeignKey('role.id'))
    
    def __init__(self, name, email, id_role):
        self.name = name
        self.email = email
        self.id_role = id_role