from app.extensions import db

class RelationDeveloperProduct(db.Model):
    __tablename__ = 'relation_developer_product'
    
    id_developer = db.Column('id_developer', db.Integer, db.ForeignKey('developer.id'), primary_key=True)
    id_product = db.Column('id_product', db.Integer, db.ForeignKey('product.id'), primary_key=True)
    
    def __init__(self, id_developer, id_product):
        self.id_developer = id_developer
        self.id_product = id_product