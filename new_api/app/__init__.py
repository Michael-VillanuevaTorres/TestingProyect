from flask import Flask

from config import Config
from app.extensions import db
from flask_cors import CORS

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    CORS(app)

    # Initialize Flask extensions here

    db.init_app(app)
        
    # Register blueprints here
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    
    from app.reassignment import bp as admin_bp
    app.register_blueprint(admin_bp, url_prefix='/reassignment')
    
    from app.user import bp as user_bp
    app.register_blueprint(user_bp, url_prefix='/user')
    
    from app.developer import bp as developer_bp
    app.register_blueprint(developer_bp, url_prefix='/developer')
    
    from app.product import bp as product_bp
    app.register_blueprint(product_bp, url_prefix='/product')
    
    from app.report import bp as report_bp
    app.register_blueprint(report_bp, url_prefix='/report')
    
    
    from app.models.comment import Comment
    from app.models.developer import Developer
    from app.models.like import Like
    from app.models.priority import Priority
    from app.models.product import Product
    from app.models.reassignment import Reassignment
    from app.models.relationship_developer_product import RelationshipDeveloperProduct
    from app.models.relationship_user_product import RelationshipUserProduct 
    from app.models.report import Report
    from app.models.role import Role
    from app.models.state import State
    from app.models.user import User
    
    with app.app_context():
        db.create_all()

    return app