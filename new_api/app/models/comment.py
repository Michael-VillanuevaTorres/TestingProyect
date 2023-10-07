from app.extensions import db

class Comment(db.Model):
    __tablename__ = 'comment'
    
    id        = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    content   = db.Column('content', db.String(10000))
    id_user   = db.Column('id_user', db.Integer, db.ForeignKey('user.id'))
    id_report = db.Column('id_report', db.Integer, db.ForeignKey('report.id'))
    date      = db.Column('date', db.DateTime, default=db.func.current_timestamp())
    
    def __init__(self, content, id_report):
        self.content = content
        self.id_report = id_report