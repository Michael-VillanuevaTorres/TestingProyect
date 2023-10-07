from app.extensions import db

class Like(db.Model):
    __tablename__ = 'like'
    
    id_developer = db.Column('id_user', db.Integer, db.ForeignKey('user.id'), primary_key=True)
    id_report    = db.Column('id_report', db.Integer, db.ForeignKey('report.id'), primary_key=True)
    
    def __init__(self, id_developer, id_report):
        self.id_developer = id_developer
        self.id_report = id_report