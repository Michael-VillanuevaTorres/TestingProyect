from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_db(app):
    from app.models.comment import Comment
    from app.models.developer import Developer
    from app.models.like import Like
    from app.models.priority import Priority
    from app.models.product import Product
    from app.models.reassignment import Reassignment
    from app.models.relation_developer_product import RelationDeveloperProduct
    from app.models.relation_user_product import RelationUserProduct 
    from app.models.report import Report
    from app.models.role import Role
    from app.models.state import State
    from app.models.user import User
    
    with app.app_context():
        db.create_all()
    
    