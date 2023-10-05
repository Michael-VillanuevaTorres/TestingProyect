from app.extensions import db

class RelationUserProduct(db.Model):
    __tablename__ = 'relation_user_product'
   
    id_user    = db.Column('id_user', db.Integer, db.ForeignKey('user.id'), primary_key=True)
    id_product = db.Column('id_product', db.Integer, db.ForeignKey('product.id'), primary_key=True)
    
    def __init__(self, id_user, id_product):
        self.id_user = id_user
        self.id_product = id_product