from app.extensions import db

class Priority(db.Model):
    __tablename__ = 'priority'
    
    id   = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('name', db.String(45))
    
    def __init__(self, name):
        self.name = name