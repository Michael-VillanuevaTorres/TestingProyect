from app.extensions import db

class User(db.Model):
    __tablename__ = 'user'
    
    id    = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name  = db.Column('name', db.String(45))
    email = db.Column('email', db.String(45))
    
    def __init__(self, name, email):
        self.name = name
        self.email = email