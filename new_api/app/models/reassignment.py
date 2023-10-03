from app.extensions import db

class Reassignment(db.Model):
    __tablename__ = 'reassignment'
    
    id_developer = db.Column('id_developer', db.Integer, db.ForeignKey('developer.id'), primary_key=True)
    id_report    = db.Column('id_report', db.Integer, db.ForeignKey('report.id'), primary_key=True)
    reason       = db.Column('reason', db.String(10000))
    date         = db.Column('date', db.DateTime, default=db.func.current_timestamp())
    
    def __init__(self, id_report, id_developer, reason):
        self.id_report = id_report
        self.id_developer = id_developer
        self.reason = reason