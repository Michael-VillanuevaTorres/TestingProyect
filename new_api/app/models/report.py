from app.extensions import db

class Report(db.Model):
    __tablename__ = 'report'
    
    id           = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    title        = db.Column('title', db.String(45))
    description  = db.Column('description', db.String(10000))
    id_developer = db.Column('id_developer', db.Integer, db.ForeignKey('developer.id'))
    id_state     = db.Column('id_state', db.Integer, db.ForeignKey('state.id'), default=0)
    id_priority  = db.Column('id_priority', db.Integer, db.ForeignKey('priority.id'), default=0)
    likes        = db.Column('likes', db.Integer, default=0)
    id_product   = db.Column('id_product', db.Integer, db.ForeignKey('product.id'))
    date         = db.Column('date', db.DateTime, default=db.func.current_timestamp())
    id_user      = db.Column('id_user', db.Integer, db.ForeignKey('user.id'))
    
    def __init__(self, title, description, id_product, id_user):
        self.title = title
        self.description = description
        self.id_product = id_product
        self.id_user = id_user
        
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'id_developer': self.id_developer,
            'id_state': self.id_state,
            'id_priority': self.id_priority,
            'likes': self.likes,
            'id_product': self.id_product,
            'date': self.date,
            'id_user': self.id_user
        }
    
    def add_state(self, id_state):
        self.id_state = id_state
    
    def add_priority(self, id_priority):
        self.id_priority= id_priority
    
    def add_developer(self, id_developer):
        self.id_developer = id_developer
    
    def add_likes(self, like):
        self.likes = self.likes + like